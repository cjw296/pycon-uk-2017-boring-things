import logging
import os

from argparse import ArgumentParser, Namespace
from mush import attr
from psycopg2.extensions import connection as Psycopg2Connection

logger = logging.getLogger(__name__)


def add_args(parser: ArgumentParser):
    parser.add_argument('path', help='Path to the file to process')


def insert_note(path: attr(Namespace, 'path'), conn: Psycopg2Connection):
    filename = os.path.basename(path)
    with open(path) as source:
        logger.debug('opened %s to insert as %s', path, filename)
        cursor = conn.cursor()
        cursor.execute('insert into notes values (%s, %s)',
                       (filename, source.read()))
    logger.info('successfully inserted %s', filename)
