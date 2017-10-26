import logging
import os

logger = logging.getLogger(__name__)

def insert_note(path, conn):
    filename = os.path.basename(path)
    with open(path) as source:
        logger.debug('opened %s to insert as %s', path, filename)
        cursor = conn.cursor()
        cursor.execute('insert into notes values (%s, %s)',
                       (filename, source.read()))
    logger.info('successfully inserted %s', filename)
