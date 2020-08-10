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
    cur_help.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id =states.id WHERE states.name = %s ORDER BY cities.id", (sys.argv[4],))
    states = cur_help.fetchall()
    val_help = ""
    for navigate in range(len(states)):
        if navigate != len(states) - 1:
            val_help += states[navigate][0] + ", "
        else:
            val_help += states[navigate][0]
    print(val_help)
    cur_help.close()
    db.close()
