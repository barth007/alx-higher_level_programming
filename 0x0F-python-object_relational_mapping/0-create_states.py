#!/usr/bin/python3
import MySQLdb

connection = MySQLdb.connect(host = 'localhost', user = 'root', password = 'Pass@12345', database = 'hbtn_0e_0_usa')
cursors = connection.cursor()
cursors.execute("CREATE TABLE IF NOT EXISTS states\
        (id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL)\
        ")
us_states = ('California', 'Arizona', 'Texas', 'New York', 'Nevada')
for state in us_states:
    cursors.execute("INSERT INTO states(name) VALUES (%s)", (state,))
connection.commit()
cursors.close()
connection.close()
