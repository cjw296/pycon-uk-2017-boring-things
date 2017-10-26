import os
import psycopg2
import pytest
from code.insert_note import insert_note

from testfixtures import TempDirectory, LogCapture, compare


@pytest.fixture(autouse=True)
def log():
    with LogCapture() as log:
        yield log

@pytest.fixture(autouse=True)
def dir():
    with TempDirectory() as dir:
        yield dir

@pytest.fixture(autouse=True, scope='module')
def conn():
    conn = psycopg2.connect(dbname=os.environ.get('DB_NAME'),
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASSWORD'))
    cursor = conn.cursor()
    cursor.execute('drop table if exists notes')
    cursor.execute('create table notes (filename varchar, text varchar)')
    yield conn
    conn.rollback()


def test_insert_note(dir, conn, log):

    file_path = dir.write('file.txt', encoding='utf-8', data='my note')

    insert_note(file_path, conn)

    cursor = conn.cursor()
    cursor.execute('select * from notes')
    compare(cursor.fetchall(), expected=[
        ('file.txt', 'my note')
    ])

    log.check(
        ('code.insert_note', 'DEBUG',
         'opened {} to insert as file.txt'.format(file_path)),
        ('code.insert_note', 'INFO', 'successfully inserted file.txt')
    )
