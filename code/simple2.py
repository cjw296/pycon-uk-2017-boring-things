import os, sqlite3, sys

if sys.argv[2] == 'prod':
    db = 'mycoolapp.db'
else:
    db = 'mycoolapp-test.db'

conn = sqlite3.connect(db)

filename = os.path.basename(sys.argv[1])
with open(sys.argv[1]) as source:
    conn.execute('insert into notes values (?, ?)',
                 (filename, source.read()))
conn.commit()
