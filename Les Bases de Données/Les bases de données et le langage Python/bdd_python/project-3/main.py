import sqlite3
import sys
import hashlib


def old_way(args: list, con, cur):
    if len(args) > 1 and len(args) < 3:
        if args[1] == "login":
            login(con, cur)
        elif args[1] == "create":
            create_user(con, cur)
        else:
            print(get_help())
            cur.close()
            con.close()
    else:
        print(get_help())

        cur.close()
        con.close()


def menu(con, cur):
    choices = [
        {
            "key": "Login",
            "desc": "You can login to retrieve your passphrase.",
            "function": login
        },
        {
            "key": "Create",
            "desc": "You can create a user and store a passphrase",
            "function": create_user
        }
    ]

    choice_index = -1

    for ind in range(len(choices)):
        _choice = choices[ind]
        print(f"{[ind]}: ", _choice["key"], _choice["desc"])

    run = True
    while run:
        choice_index = int(input("Select which method to use [0-1]: "))

        try:
            choices[choice_index]["function"](con, cur)
            run = False
        except IndexError:
            continue


def main():

    args = sys.argv

    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT UNIQUE NOT NULL, passwd TEXT NOT NULL, passphrase TEXT NOT NULL)")

    # old_way(args, con, cur)
    menu(con, cur)


def get_help():
    return "users <login|create>"


def hash_passwd(passwd: str):
    md5 = hashlib.md5()
    md5.update(bytes(passwd, 'ascii'))
    return md5.hexdigest()


def check_passwd(hashed_passwd: str, db_passwd: str):
    return hashed_passwd == db_passwd


def login(con, cur):
    run = True
    tries = 1

    while run and tries < 4:
        login = str(input("Login: "))

        istrue = cur.execute(
            "SELECT COUNT(*) FROM Users WHERE login=?", (login,)).fetchone()[0]

        if istrue == 0:
            print("Login doesn't exist.")
            continue

        passwd = str(input("Password: "))

        hashed_passwd = str(hash_passwd(passwd))

        is_passwdcorrect = cur.execute(
            "SELECT passphrase FROM Users WHERE login=? AND passwd=?", (login, hashed_passwd)).fetchone()

        if is_passwdcorrect == None:
            if tries > 2:
                run = False
            print(f"Tries {tries}/3")
            tries += 1
        else:
            print(is_passwdcorrect[0])
            run = False


def create_user(con, cur):
    run = True
    while run:
        login = str(input("Please input a new username: "))

        if len(login) < 5:
            print("Login is too short")
            continue

        has_login = cur.execute(
            "SELECT COUNT(*) AS count FROM Users WHERE login=?", (login,)).fetchone()[0]

        if has_login > 0:
            print("User already exists.")
            continue

        passwd = str(input("Please input your password: "))

        if len(passwd) < 4:
            print("Password too short.")
            continue

        passphrase = str(input("Please input a passphrase: "))
        if len(passphrase) < 4:
            print("Passphrase too short.")
            continue

        hashed_passwd = str(hash_passwd(passwd))

        cur.execute("INSERT INTO Users (login, passwd, passphrase) VALUES (?, ?, ?)",
                    (login, hashed_passwd, passphrase))

        con.commit()
        run = False

    cur.close()
    con.close()


if __name__ == "__main__":
    main()
