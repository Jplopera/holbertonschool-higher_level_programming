#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT t1.id, t1.name, t2.name \
             FROM cities t1 \
             LEFT JOIN states t2 \
             ON t1.state_id = t2.id \
             WHERE t2.name = '{}' \
             ORDER BY t1.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    db.close()
