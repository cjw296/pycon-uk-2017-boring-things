from argparse import ArgumentParser
from configparser import RawConfigParser
import logging, os, psycopg2, sys

def script():
    parser = ArgumentParser()
    parser.add_argument('config', help='Path to .ini file')
    parser.add_argument('path', help='Path to the file to process')
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--db-name')
    parser.add_argument('--db-user')
    parser.add_argument('--db-pass')
    args = parser.parse_args()

    config = RawConfigParser()
    config.read(args.config)

    handler = logging.FileHandler(config.get('main', 'log'))
    handler.setLevel(logging.DEBUG)
    log = logging.getLogger()
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    if not args.quiet:
        handler = logging.StreamHandler(sys.stderr)
        handler.setLevel(logging.DEBUG if args.verbose else logging.INFO)
        log.addHandler(handler)

    db = args.db_name or os.environ.get('DB_NAME') or config.get('db', 'name')
    user = args.db_user or os.environ.get('DB_USER') or config.get('db', 'user')
    password = args.db_pass or os.environ.get('DB_PASS') or config.get('db', 'password')

    log.debug('connecting to %s as %s', db, user)
    conn = psycopg2.connect(dbname=db, user=user, password=password)

    filename = os.path.basename(args.path)
    with open(args.path) as source:
        log.debug('opened %s to insert as %s', args.path, filename)
        cursor = conn.cursor()
        cursor.execute('insert into notes values (%s, %s)',
                       (filename, source.read()))
    conn.commit()
    log.info('successfully inserted %s', filename)

if __name__ == '__main__':
    script()
