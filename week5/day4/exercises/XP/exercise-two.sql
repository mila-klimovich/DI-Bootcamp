SELECT * FROM customer

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer

SELECT DISTINCT create_date FROM customer

SELECT * FROM customer ORDER BY first_name DESC

SELECT film_id, title, description, release_year, rental_rate 
FROM film
ORDER BY rental_rate ASC

SELECT address, phone FROM address WHERE district = 'Texas'

SELECT * FROM film WHERE film_id IN (15, 150)

SELECT 
	film_id,
	title,
	description,
	length,
	rental_rate
FROM
	film
WHERE 
    title = 'Forest Gump'

SELECT 
	film_id,
	title,
	description,
	length,
	rental_rate
FROM
	film
WHERE 
    title LIKE 'Fo%'

SELECT * FROM film ORDER BY replacement_cost ASC LIMIT 10

SELECT * FROM film ORDER BY replacement_cost ASC LIMIT 10 OFFSET 10

SELECT * FROM customer
SELECT * FROM payment

SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id
ORDER BY customer.customer_id

SELECT film_id, title FROM film WHERE film.film_id NOT IN (SELECT film_id FROM inventory)

SELECT city.city, country.country 
FROM city
INNER JOIN country
ON city.country_id = country.country_id

SELECT * FROM staff
SELECT * FROM customer
SELECT * FROM payment

SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date, staff.staff_id
FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id
INNER JOIN staff ON customer.store_id = staff.store_id
ORDER BY staff_id