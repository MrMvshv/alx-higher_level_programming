-- create db & table on server
-- should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    PRIMARY KEY(`id`),
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_cities_states_id
        FOREIGN KEY (state_id)
        REFERENCES states(id)
);
