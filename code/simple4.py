from configparser import RawConfigParser
import os, psycopg2, sys

if sys.argv[2] == 'prod':
    db = 'mycoolapp.db'
else:
    db = 'mycoolapp-test.db'

config = RawConfigParser()
config.read(sys.argv[1])
user = config.get('db', 'user')
password = config.get('db', 'password')

print('connecting to {} as {}', db, user)
conn = psycopg2.connect(dbname=db, user=user, password=password)

filename = os.path.basename(sys.argv[3])
with open(sys.argv[3]) as source:
    print('opened {} to insert as {}', sys.argv[3], filename)
    conn.execute('insert into notes values (?, ?)',
                 (filename, source.read()))
conn.commit()
print('yay!')
