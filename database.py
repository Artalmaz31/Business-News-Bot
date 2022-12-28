import sqlite3
from config import DB_NAME

def add_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("INSERT INTO USERS (ID) VALUES (%s)" % (user_id))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute("SELECT ID from USERS")
    users = list()
    for row in cursor:
        users.append(row[0])
    conn.close()
    return users

def update_news(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute("SELECT TITLE from NEWS")
    last_news = str()
    flag = False
    for row in cursor:
        flag = True
        last_news = row[0]

    if not flag:
        conn.execute("INSERT INTO NEWS (TITLE) VALUES ('NEWS')")
        conn.commit()
    if title == last_news:
        conn.close()
        return 0
    else:
        conn.execute("UPDATE NEWS SET TITLE = '%s'" % (title))
        conn.commit()
        conn.close()
        return 1

def update_advice(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.execute("SELECT TITLE from ADVICE")
    last_news = str()
    flag = False
    for row in cursor:
        flag = True
        last_news = row[0]

    if not flag:
        conn.execute("INSERT INTO ADVICE (TITLE) VALUES ('ADVICE')")
        conn.commit()
    if title == last_news:
        conn.close()
        return 0
    else:
        conn.execute("UPDATE ADVICE SET TITLE = '%s'" % (title))
        conn.commit()
        conn.close()
        return 1