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

teachers = {}
people = {}

cur.execute("SELECT * FROM user;")
res = cur.fetchall()
conn.commit()
print(res)


def id_from_data():
    cur.execute("""SELECT userid, user_name FROM user WHERE status != 'teacher'""")
    data = cur.fetchall()
    conn.commit()
    for repacking in data:
        got_id, user_name = repacking
        people[got_id] = user_name
    return people

def teacher_from_data():
    cur.execute("""SELECT userid, user_name FROM user WHERE status = 'teacher'""")
    data = cur.fetchall()
    conn.commit()
    for repacking in data:
        got_id, user_name = repacking
        teachers[got_id] = user_name
    return teachers
