#!/usr/bin/python3
import sys
import MySQLdb

"""The script lists all states from the database hbtn_0e_0_usa and takes
   three commandline arguments

   Args:
      mysql username;
      mysql password;
      database name;
"""
db_user = sys.argv[1]
db_password = sys.argv[2]
data_base = sys.argv[3]
db_host = "localhost"
db_port = 3306

connection = MySQLdb.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=data_base,
        port=db_port
        )
cursors = connection.cursor()
cursors.execute("SELECT * FROM states WHERE id ORDER BY id ASC")
rows = cursors.fetchall()
for row in rows:
    print("{}".format(row))
cursors.close()
connection.close()
