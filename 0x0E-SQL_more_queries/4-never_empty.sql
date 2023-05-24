-- This script creates a tabel id_not_null on your MySQL server where id as a default
-- value of 1
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
