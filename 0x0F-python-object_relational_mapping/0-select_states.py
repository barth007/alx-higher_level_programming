#!/usr/bin/python3
# The script lists all states from the database hbtn_0e_0_usa and takes
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import sys
import MySQLdb

if __name__ == '__main__':
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
    rows = cursors.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in range(rows):
        print(cursors.fetchone())
    cursors.close()
    connection.close()
