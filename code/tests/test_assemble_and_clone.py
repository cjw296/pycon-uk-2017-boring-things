import os
from argparse import ArgumentParser

import psycopg2
import pytest
from mush import Runner

from code.assemble_and_clone import main

from testfixtures import TempDirectory, LogCapture, compare


@pytest.fixture(autouse=True)
def log():
    with LogCapture(attributes=('levelname', 'getMessage')) as log:
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

def run_with(main, conn, argv):
    runner = Runner(ArgumentParser)
    runner.extend(main.clone(added_using='args'))
    runner.add(lambda parser: parser.parse_args(argv),
               requires=ArgumentParser)
    runner.add(lambda: conn)
    runner.extend(main.clone(start_label='body'))
    runner()

def test_script(dir, conn, log):

    file_path = dir.write('file.txt', encoding='utf-8', data='my note')

    run_with(main, conn, argv=[file_path])

    cursor = conn.cursor()
    cursor.execute('select * from notes')
    compare(cursor.fetchall(), expected=[
        ('file.txt', 'my note')
    ])

    log.check(
        ('DEBUG', 'opened {} to insert as file.txt'.format(file_path)),
        ('INFO', 'successfully inserted file.txt')
    )
