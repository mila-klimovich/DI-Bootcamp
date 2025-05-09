CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)


INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
	('Mila','Klimovich','28/10/1989', 999),
	('Lina','Babich','01/10/1999', 0),
	('Frida','Green','05/05/2005', 2);


SELECT
   first_name,
   last_name,
   age
FROM
   actors;

SELECT * FROM actors WHERE first_name != 'Matt' ;
SELECT * FROM actors WHERE number_oscars >= 1 OR last_name = 'Klimovich';
SELECT * FROM actors WHERE last_name LIKE '%mov%';

SELECT * FROM actors ORDER BY number_oscars DESC LIMIT 1 OFFSET 1;
SELECT * FROM actors WHERE age > '1960-01-01' ORDER BY age DESC

SELECT * FROM actors ORDER BY last_name DESC LIMIT 4
SELECT * FROM actors WHERE first_name LIKE '%e%'
SELECT * FROM actors WHERE number_oscars >= 5

UPDATE actors SET age='1970-01-01' WHERE first_name='Matt' AND last_name='Damon';

UPDATE actors 
SET age='1970-01-01' 
WHERE first_name='Matt' AND last_name='Damon'
RETURNING 
    actor_id,
    first_name, 
    last_name,
    age;

DELETE FROM actors WHERE actor_id=4
RETURNING actor_id, first_name, last_name, number_oscars;

ALTER TABLE actors RENAME COLUMN age TO date_of_birth;
SELECT * FROM actors;