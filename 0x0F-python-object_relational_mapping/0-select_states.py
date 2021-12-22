#!/usr/bin/python3
import MySQLdb
from sys import argv
"""
A python script that displays all state names
from hbtn_0e_0_usa database
"""
# Open database connection
myconn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         port=3306, db=argv[3])

# Preparing a cursor object using a cursor method
cur = myconn.cursor()
# Preparing a query that gets all state names
sql = """SELECT * FROM states"""
try:
    # Executing the sql command
    cur.execute(sql)
    # Commiting changes in the database
    results = cur.fetchall()
    # Fetcthing all names in states
    for row in cur:
        print(row)
except Exception:
    print("Unable to fetch data")

# Closing the database connection
myconn.close()
