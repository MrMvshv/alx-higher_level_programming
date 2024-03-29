#!/usr/bin/python3
""" lists all states from
    database hbtn_0e_0_usa
    using module MySQLdb
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
