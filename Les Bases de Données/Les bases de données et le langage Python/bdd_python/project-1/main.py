
import sqlite3
import sys


def help_grades():
    print("grades <insert|list>")


def main():
    args = sys.argv
    if len(args) > 1 and len(args) < 3:
        command = args[1]

        con = sqlite3.connect("grades.db")
        cur = con.cursor()

        if command.lower() == "insert":
            insert(con, cur)
        elif command.lower() == "list":
            list_values(con, cur)
        else:
            help_grades()
    else:
        help_grades()


def insert(con, cur):

    cur.execute(
        "CREATE TABLE IF NOT EXISTS Grades (id INTEGER PRIMARY KEY AUTOINCREMENT, grade INTEGER NOT NULL, name TEXT NOT NULL)")

    run = True

    while run:
        try:
            name = str(input("Input a name: "))

            if name.lower() == "q":
                run = False

            else:
                grade = int(input("Input a grade: "))

                cur.execute(
                    "INSERT INTO Grades (grade, name) VALUES (?, ?)", (name, grade))
                l = cur.execute("SELECT * FROM Grades").fetchall()

                for row in l:
                    print(row)

                con.commit()

        except ValueError:
            continue

    cur.close()
    con.close()


def list_values(con, cur):
    grades = cur.execute("SELECT * FROM Grades").fetchall()

    for row in grades:
        print(row)

    cur.close()
    con.close()


if __name__ == "__main__":
    main()
