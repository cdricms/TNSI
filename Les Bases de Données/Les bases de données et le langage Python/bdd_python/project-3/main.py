import sqlite3


def main():

    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT UNIQUE NOT NULL, passwd TEXT NOT NULL, passphrase TEXT NOT NULL)")


def login(con, cur):
    run = True
    tries = 1

    while run and tries < 4:
        login = str(input("Login: "))
        passwd = str(input("Password: "))

        istrue = cur.execute(
            "SELECT COUNT(*) FROM Users WHERE login=?", (login,)).fetchone()[0]

        if istrue == 0:


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

        cur.execute("INSERT INTO Users (login, passwd, passphrase) VALUES (?, ?, ?)",
                    (login, passwd, passphrase))

        con.commit()

    cur.close()
    con.close()


if __name__ == "__main__":
    main()
