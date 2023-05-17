--  This script creates a table called firsttable in the current database in MySQL server.
--  Attributes:
-- id INT,
-- name VARCHAR(256)
-- if the table firsttable already exists, the script fails.

CREATE TABLE IF NOT EXISTS `first_name`(
    `id` int,
    `name` varchar(256)
    )
