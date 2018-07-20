import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute(r"insert into user (id, name) values ('2', 'Penn')")
cursor.close()
conn.commit()
conn.close()
