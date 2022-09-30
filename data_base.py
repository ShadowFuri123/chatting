import sqlite3

conn = sqlite3.connect('all.db', check_same_thread=False)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users5(
   userid INT PRIMARY KEY,
   status TEXT,
   reply TEXT,
   user_name TEXT
   class TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS admin(
    id INT PRIMARY KEY
    name TEXT);
    """)

cur.execute("SELECT * FROM users5;")
res = cur.fetchall()
conn.commit()
print(res)

