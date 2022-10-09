import sqlite3

conn = sqlite3.connect('all.db', check_same_thread=False)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user(
   userid INT PRIMARY KEY,
   status TEXT,
   reply TEXT,
   user_name TEXT
   clas TEXT);
""")
conn.commit()



cur.execute("SELECT * FROM user;")
res = cur.fetchall()
conn.commit()
print(res)
