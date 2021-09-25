DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capital VARCHAR(255),
    continent VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE cities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    info VARCHAR(255),
    sight VARCHAR(255),
    visited BOOLEAN,
    countries_id INT REFERENCES countries(id)
);