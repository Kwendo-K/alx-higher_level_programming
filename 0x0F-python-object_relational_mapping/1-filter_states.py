#!/usr/bin/python3
import MySQLdb

# Python script that displays state names starting with N
# Myconn is a varible that stores mysql connection
#

myconn = MySQLdb.connect(host="localhost", user="root", passwd="Asila@1991",
                         port=3306, db="hbtn_0e_0_usa")
cur = myconn.cursor()

try:
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
except Exception:
    myconn.rollback()

for row in rows:
    print(row)

cur.close()
myconn.close()
