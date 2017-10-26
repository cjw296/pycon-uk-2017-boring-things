from code.testable1 import script

from testfixtures import TempDirectory, OutputCapture, compare
from textwrap import dedent
import os, pytest, psycopg2
from unittest import mock

@pytest.fixture(autouse=True)
def dir():
    with TempDirectory() as dir:
        yield dir

@pytest.fixture(autouse=True, scope='module')
def cursor():
    conn = psycopg2.connect(dbname=os.environ.get('DB_NAME'),
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASSWORD'))
    cursor = conn.cursor()
    cursor.execute('drop table if exists notes')
    cursor.execute('create table notes (filename varchar, text varchar)')
    conn.commit()
    yield cursor

def test_script(dir, cursor):
    config_path = dir.write('config.ini', encoding='utf-8', data=dedent("""
    [main]
    log={log}
    
    [db]
    name={name}
    user={user}
    password={password}
    """.format(log=dir.getpath('log.txt'),
               name=os.environ.get('DB_NAME'),
               user=os.environ.get('DB_USER'),
               password=os.environ.get('DB_PASSWORD'))))

    file_path = dir.write('file.txt', encoding='utf-8', data='my note')

    with mock.patch('sys.argv', ['x', config_path, file_path]):
        with OutputCapture() as output:
            script()

    cursor.execute('select * from notes')
    compare(cursor.fetchall(), expected=[
        ('file.txt', 'my note')
    ])

    output.compare(
        'successfully inserted file.txt'
    )
