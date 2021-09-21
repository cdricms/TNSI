import sqlite3

conn = sqlite3.connect("baseDonnees.db")
cur = conn.cursor()
cur.execute("CREATE TABLE LIVRES (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT, auteur TEXT, ann_publi INTEGER, note INTEGER)")
cur.execute("INSERT INTO LIVRES(id, titre, auteur, ann_publi, note)
            VALUES(1, '1984', 'Orwell', 1949, 10)")
cur.close()
conn.close()
