#!/usr/bin/python3

from sys import argv
import MySQLdb


def lists_states(db_user, db_password, data_base):
    """
        The script lists all states from the database hbtn_0e_0_usa and takes
        Usage: ./0-select_states.py <mysql username> \
                                    <mysql password> \
                                    <database name>
      Args:
          db_user(database user)
          db_password(database password)
          data_base(database)
    """
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
    cursors.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursors.fetchall()
    for row in rows:
        print(row)
    cursors.close()
    connection.close()


if __name__ == "__main__":
    lists_states(argv[1], argv[2], argv[3])
