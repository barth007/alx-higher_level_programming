-- This script lists all the tables of a database in the MySQL server.
-- The database name is passed in as command.
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'mysql';

