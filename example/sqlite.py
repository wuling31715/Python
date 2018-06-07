import sqlite3

con = sqlite3.connect('gpa.sqlite')


def insert(credit, score, gpa):
    con.execute(
        'INSERT INTO "main"."grade" ("credit","score","gpa") VALUES (%f, %f, %f)'
        % (credit, score, gpa))


def select():
    select = con.execute('SELECT * FROM "main"."grade"')
    for row in select:
        print row


def delete():
    con.execute('DELETE FROM "main"."grade"')


delete()

con.commit()
con.close()
