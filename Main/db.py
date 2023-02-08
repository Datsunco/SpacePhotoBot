import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()


def add_user_presale(uid, latitude, longitude):
    # new user always has balance = 0
    cur.execute(f'INSERT INTO UsersPresale VALUES ({uid}, {latitude},{longitude})')
    con.commit()

def add_user(uid):
    # new user always has balance = 0
    cur.execute(f'INSERT INTO Users VALUES ({uid})')
    con.commit()

def check_user(uid):
    cur.execute(f'SELECT * FROM UsersPresale WHERE uid = {uid}')
    user = cur.fetchone()
    if user:
        return True
    return False