from argparse import ArgumentParser
from configparser import RawConfigParser
import logging, os, psycopg2, sys


parser = ArgumentParser()
parser.add_argument('config', help='Path to .ini file')
parser.add_argument('path', help='Path to the file to process')
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

db = config.get('db', 'name')
user = config.get('db', 'user')
password = config.get('db', 'password')

print('connecting to {} as {}', db, user)
conn = psycopg2.connect(dbname=db, user=user, password=password)

filename = os.path.basename(args.path)
with open(args.path) as source:
    print('opened {} to insert as {}', args.path, filename)
    conn.execute('insert into notes values (?, ?)',
                 (filename, source.read()))
conn.commit()
print('yay!')
