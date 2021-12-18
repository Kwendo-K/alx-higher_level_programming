#!/usr/bin/python3
import MySQLdb

"""
A python script that displays all the states
from hbtn_0e_0_usa
"""

myconn = MySQLdb.connect(host="localhost", user="root", passwd="Asila@1991",
                         db="hbtn_0e_0_usa")
cur = myconn.cursor()

try:
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
except Exception:
    myconn.rollback()

for row in rows:
    print(row)

cur.close()
myconn.close()
