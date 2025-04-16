SELECT * FROM actors
SELECT COUNT(*) AS actors_count FROM actors

-- For this table trying to add a new actor with some blank fields gives me an ERROR. We have NOT NULL constraint for every column

INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
VALUES
	('Bred','Pitt','28/10/1989')