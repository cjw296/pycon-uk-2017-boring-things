import os, sqlite3, sys

conn = sqlite3.connect('mycoolapp.db')

filename = os.path.basename(sys.argv[1])
with open(sys.argv[1]) as source:
    conn.execute('insert into notes values (?, ?)',
                 (filename, source.read()))
conn.commit()
