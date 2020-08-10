#!/usr/bin/python3
"""
Lists all states from the database with specifications
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db_help = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],)
    cur_help = db_help.cursor()
    cur_help.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON state_id = cities.state.id ORDER BY cities.id ASC")
    states = cur_help.fetchall()
    for navigate in states:
        print(navigate)
    cur_help.close()
    db_help.close()
