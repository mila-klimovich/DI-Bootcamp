-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
-- );

-- CREATE TABLE movies_2(
-- movie_id SERIAL PRIMARY KEY,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER
-- );


-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

-- SELECT * FROM movies

-- INSERT INTO movies_2 (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

-- SELECT * FROM actors INNER JOIN movies_2 ON actors.actor_id = movies_2.actor_playing_id

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;

-- CREATE TABLE producers(
-- producer_id SERIAL PRIMARY KEY,
-- producer_name VARCHAR (20) NOT NULL,
-- producer_last_name TEXT,
-- id_of_a_movie INTEGER,
-- FOREIGN KEY (id_of_a_movie) REFERENCES movies (movie_id)
-- );

-- SELECT * FROM movies

-- INSERT INTO producers (producer_name, producer_last_name, id_of_a_movie) VALUES
--     ( 'Scott', 'Mosier',
--     (SELECT movie_id from movies WHERE movie_title='Good Will Hunting')),
--     ( 'Jerry', 'Weintraub', 2);

-- SELECT * FROM producers

-- SELECT p.producer_name, p.producer_last_name, m.movie_title
-- FROM producers as p
-- INNER JOIN movies as m
-- ON p.id_of_a_movie = m.movie_id;

-- SELECT *--actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- LEFT JOIN movies_2
-- ON actors.actor_id = movies_2.actor_playing_id;

-- INSERT INTO movies_2 (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Fight Club', 
--     'Blah blah blah', 15);

-- SELECT *--actors.first_name, actors.last_name, movies_2.movie_title
-- FROM actors
-- RIGHT JOIN movies_2
-- ON actors.actor_id = movies_2.actor_playing_id;

-- SELECT actors.first_name, actors.last_name, movies_2.movie_title
-- FROM actors
-- FULL JOIN movies_2
-- ON actors.actor_id = movies_2.actor_playing_id;

-- SELECT avg(number_oscars) AS average_number_oscars FROM actors;

-- SELECT count (DISTINCT first_name) FROM actors;
-- SELECT max(number_oscars) AS best_actor FROM actors;
-- SELECT min(number_oscars) AS worst_actor FROM actors;

-- SELECT actors.first_name, avg(number_oscars) AS average 
-- FROM actors
-- GROUP BY actors.first_name

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES('Matt','Ross','03/01/1970', 0);

-- SELECT DISTINCT first_name FROM actors;

-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars) VALUES('George','Clooney','06/05/1961 ', 1);

-- SELECT * FROM actors

-- SELECT first_name, last_name, sum(number_oscars) FROM actors GROUP BY first_name, last_name;
SELECT first_name, sum(number_oscars) FROM actors GROUP BY first_name;

