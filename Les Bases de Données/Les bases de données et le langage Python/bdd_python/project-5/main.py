import sqlite3


def main():
    con = sqlite3.connect("livres.db")
    cur = con.cursor()

    print(list_tables(con, cur))
    print(list_values("auteur", con, cur))

    cur.close()
    con.close()


def list_values(tablename: str, con, cur, limit=20, offset=0):

    values = cur.execute(
        f"SELECT * FROM {tablename} LIMIT ? OFFSET", (limit, offset)).fetchall()

    return values


def list_tables(con, cur):
    tables_sql = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    tables = []

    for t in tables_sql:
        tables.append(t[0])

    return tables


if __name__ == "__main__":
    main()
