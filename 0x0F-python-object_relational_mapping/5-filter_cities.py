#!/usr/bin/env python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name=%s \
    ORDER BY cities.id ASC", (argv[4],))
    print(", ".join(city[0] for city in cursor.fetchall()))
    cursor.close()
    connection.close()
