zsh: 1: command not found: q


"""
Pour faire de ceci un projet complet, il faudrait rajouter beaucoup de choses, notamment vérifier pour des erreurs, notamment dans les input.
Mais cela prendrait beaucoup trop de temps à faire. Et évidemment rajouter des fonctions de bases pour modifier, supprimer etc.
"""


def main():
    con = sqlite3.connect("livres.db")
    cur = con.cursor()

    menu(con, cur)

    cur.close()
    con.close()


def menu(con, cur):
    choices = [
        {
            "desc": "List tables",
            "function": menu_list_tables,
        },
        {
            "desc": "List values from table",
            "function": menu_list_values
        },
        {
            "desc": "Insert value",
            "function": menu_insert_value
        }
    ]

    for idx, choice in enumerate(choices):
        print(f"[{idx + 1}] ", choice['desc'])

    _choice = int(input('Choice: (1, 2, 3, ...) '))

    if _choice <= len(choices) and _choice > 0:
        choices[_choice - 1]["function"](con, cur)


def menu_insert_value(con, cur):
    tables = list_tables(con, cur)

    for idx, tablename in enumerate(tables):
        print(f"[{idx + 1}] ", tablename)

    choice = int(input("Table (1, 2, 3, ...) "))

    if choice <= len(tables) and choice > 0:
        values = []
        tablename = tables[choice - 1]
        table_info = get_table_info(tablename, con, cur)
        columns_name = table_info[1]

        for column in columns_name:
            value = str(input(f"{column}: "))
            values.append(value)

        insert_value(tablename, values, con, cur)


def menu_list_tables(con, cur):
    tables = list_tables(con, cur)

    print("These are all the tables \n", tables)


def menu_list_values(con, cur):
    tables = list_tables(con, cur)

    for idx, tablename in enumerate(tables):
        print(f"[{idx + 1}] ", tablename)

    choice = int(input("Table (1, 2, 3, ...) "))

    if choice <= len(tables) and choice > 0:
        values = list_values(tables[choice - 1], con, cur)

        for value in values:
            print(value)


def get_table_info(tablename: str, con, cur):
    columns = cur.execute(f"pragma table_info({tablename})").fetchall()
    columns_name = [column[1] for column in columns]
    c = ",".join(columns_name)

    return c, columns_name


def insert_value(tablename: str, values: tuple, con, cur):
    table_info = get_table_info(tablename, con, cur)
    c = table_info[0]
    columns_name = table_info[1]
    string = f"INSERT INTO {tablename} ({c}) VALUES ({('?,' * len(columns_name))[:-1]})"
    print(string)
    cur.execute(
        string, values)

    con.commit()


def list_values(tablename: str, con, cur, limit=20, offset=0):

    values = cur.execute(
        f"SELECT * FROM {tablename} LIMIT ? OFFSET ?", (limit, offset)).fetchall()

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
