#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")
    for states in cursor.fetchall():
        print(states)
    cursor.close()
    connection.close()
