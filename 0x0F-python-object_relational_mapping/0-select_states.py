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

# Executing a query that gets all state names
try:
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
except Exception:
    myconn.rollback()

for row in rows:
    print(row)

# Closing the database connection
myconn.close()
