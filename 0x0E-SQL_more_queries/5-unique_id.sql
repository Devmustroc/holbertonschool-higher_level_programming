-- script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
id INT NOT NULL UNIQUE 1
name VARCHAR(256),
UNIQUE INDEX(id));
