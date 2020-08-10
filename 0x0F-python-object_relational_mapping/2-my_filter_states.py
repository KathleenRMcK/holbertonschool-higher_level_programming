#!/usr/bin/python3
"""
Lists all states from the database with name matching arg
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db_help = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3])
    cur_help = db_help.cursor()
    cur_help.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id asc"
                     .format(sys.argv[4]))
    states = cur_help.fetchall()
    for navigate in states:
        if navigate[1] == sys.argv[4]:
            print(navigate)
    cur_help.close()
    db_help.close()
