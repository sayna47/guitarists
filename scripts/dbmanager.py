"""This is a file for the back end user to manage the user's database."""

import sqlite3
import hashlib
import argparse
import random

db_check = 'user_database.db'
conn = 0
cursor = 0


def check_or_create(db):
    """Check if database exists in a specific file, if not create one."""
    global conn
    global cursor
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                       (username CHAR(256) NOT NULL, password CHAR(256)
                        NOT NULL,
                        salt CHAR(256) NOT NULL,
                        PRIMARY KEY (salt))''')


def parse_args():
    """Adding or checking the username."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                        "(requires -p)", required=False)
    return parser.parse_args()


def save_new_username(username, password):
    """Save new username with password."""
    global conn
    global cursor
    salt = str(random.random())
    digest = salt + password  # make the digest with password and salt
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()

    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()
    print('Username {} successfully added.'.format(username))


def check_for_username(username, password, db):
    """Check for validity of username and password."""
    global conn
    global cursor
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    # first, check if the username is there
    try:
        cursor.execute("SELECT username FROM user WHERE username=?",
                       (username, )).fetchall()[0]
    except:
        print('Username is not valid')
        return
    salt = cursor.execute("SELECT salt FROM user WHERE username=?",
                          (username, ))
    results = salt.fetchone()
    digest = (results[0]) + password
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM user WHERE username=? and "
                          "password=?", (username, digest))
    conn.commit()
    results = rows.fetchall()
    if results:
        print ("User is present, password is valid")
        return True
    else:
        print ("Password is invalid")
        return False

if __name__ == "__main__":
    check_or_create(db_check)
    parse_args()
    args = parse_args()
    if args.a and args.p:
        save_new_username(args.a, args.p)
    elif args.c and args.p:
        check_for_username(args.c, args.p, db_check)
    conn.close()
