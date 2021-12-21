#!/usr/bin/python3
import MySQLdb
"""
A python script that displays all state names
from hbtn_0e_0_usa database
"""
# Open database connection
myconn = MySQLdb.connect(host="localhost", user="root", passwd="Asila@1991",
                         db="hbtn_0e_0_usa")

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
