-- This script lists all the cities of California 
-- that can be found in the database hbtn_0d_usa.
SELECT c.id, c.name FROM cities AS c
WHERE 
state_id = (SELECT id FROM states AS s WHERE s.name = "California");
