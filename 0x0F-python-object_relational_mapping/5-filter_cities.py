#!/usr/bin/python3
""" lists all states with a name N..
    from database hbtn_0e_0_usa
    using module MySQLdb
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cmd = "SELECT cities.name \
        FROM cities INNER JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name LIKE %s ORDER BY cities.id ASC;"
    para = (sys.argv[4],)
    cur.execute(cmd, para)

    query_rows = cur.fetchall()
    cities = ', '.join([row[0] for row in query_rows])
    print(cities)

    cur.close()
    db.close()
