-- create table on server
-- should not fail
CREATE TABLE IF NOT EXISTS force_name (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256) NOT NULL);
