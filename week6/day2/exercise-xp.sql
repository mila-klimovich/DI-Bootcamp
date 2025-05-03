-- Exercise 1

SELECT * FROM language

SELECT * FROM film

-- Get a list of all films joined with their languages 
-- – select the following details : film title, description, and language name.

SELECT film.title, film.description, language.name
FROM film
INNER JOIN language
ON film.language_id = language.language_id

-- Get all languages, even if there are no films in those languages 
-- – select the following details : film title, description, and language name.

SELECT film.title, film.description, language.name
FROM film
RIGHT JOIN language
ON film.language_id = language.language_id

-- Create a new table called new_film with the following columns : id, name. 
-- Add some new films to the table.

CREATE TABLE new_film(
id SERIAL,
name VARCHAR (50) NOT NULL,
PRIMARY KEY (id)
)

INSERT INTO new_film (id, name) 
VALUES
	(1, 'Memories of murder'),
	(2, 'OLDBOY'),
	(3, 'Train to Busan');

SELECT * FROM new_film

CREATE TABLE customer_review(
review_id SERIAL NOT NULL PRIMARY KEY,
film_id SMALLINT REFERENCES new_film(id) ON DELETE CASCADE,
language_id SMALLINT REFERENCES language(language_id),
title VARCHAR (20) NOT NULL,
score SMALLINT CHECK (score BETWEEN 1 AND 10),
review_text TEXT,
last_update DATE
)

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
	(1, 3, 'Recommend!', 9, 'Great movie', '03-05-2025'),
	(2, 3, 'Scary!!!', 10, 'Loved it', '02-02-2022')


SELECT * FROM customer_review

DELETE FROM new_film
WHERE id = 1

-- Exercise 2
SELECT * FROM language
SELECT * FROM film WHERE film_id = 1

UPDATE film
SET language_id = CASE
	WHEN film_id = 1 THEN 2
	WHEN film_id = 2 THEN 3
	WHEN film_id = 3 THEN 2
	ELSE language_id
END
WHERE film_id IN (1, 2, 3);

SELECT * FROM film WHERE film_id IN (1, 2, 3)

SELECT * FROM customer
-- for customer table FK store_id and address_id are defined. 
-- When we INSERT we need to make sure to provide a value that already exists in the reference table 

DROP TABLE customer_review
-- easy to execute but needs to be checked. if other table reference it i'll get an error
-- can also affect other tables

SELECT * FROM rental

SELECT COUNT(*) FROM rental
WHERE return_date = NULL

-- SELECT * FROM inventory
-- SELECT * FROM film

SELECT film.title, film.rental_rate 
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE rental.return_date = NULL
ORDER BY rental_rate DESC 
LIMIT 30;

-- SELECT * FROM film_actor

SELECT film.title, film.description, actor.first_name, actor.last_name
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe'
  AND film.description ILIKE '%sumo%';

-- SELECT * FROM film
-- SELECT * FROM category

SELECT film.title, film.length, film.rating, category.name AS category
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.length < 60
  AND film.rating = 'R'
  AND category.name = 'Documentary';

-- SELECT * FROM payment

SELECT film.title, payment.amount, rental.return_date, customer.first_name, customer.last_name
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN payment ON rental.rental_id = payment.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND payment.amount > 4.00
  AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT film.title, film.description, film.replacement_cost
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND film.description ILIKE '%boat%'
ORDER BY film.replacement_cost DESC
LIMIT 1;