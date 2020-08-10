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
                              db=sys.argv[3])
    cur_help = db.cursor()
    cur_help.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = state.id ORDER BY id asc")
    states = cur_help.fetchall()
    for navigate in states:
        print(navigate)
    cur_help.close()
    db.close()
