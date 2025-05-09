-- Exercise 1
SELECT r.rental_id, r.rental_date, i.film_id, f.title
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL;

SELECT c.customer_id, c.first_name, c.last_name, COUNT(*) AS outstanding_rentals
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY outstanding_rentals DESC;

SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE c.name = 'Action'
  AND a.first_name = 'Joe' AND a.last_name = 'Swank';

--OR create a view
CREATE VIEW film_actor_category_view AS
SELECT f.title, a.first_name, a.last_name, c.name AS category
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id;

SELECT title
FROM film_actor_category_view
WHERE category = 'Action'
  AND first_name = 'Joe' AND last_name = 'Swank';

-- Exercise 2
SELECT s.store_id, ci.city, co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

SELECT s.store_id,
       SUM(f.length) AS total_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
       ROUND(SUM(f.length) / 60.0 / 24.0, 2) AS total_days
FROM store s
JOIN inventory i ON s.store_id = i.store_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NOT NULL
GROUP BY s.store_id;

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
    SELECT a.city_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
);

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
    SELECT co.country_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
);

SELECT COUNT(*) AS total_safe_films,
       SUM(f.length) AS total_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
       ROUND(SUM(f.length) / 60.0 / 24.0, 2) AS total_days
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name != 'Horror'
  AND f.title NOT ILIKE ANY (ARRAY[
        '%beast%', '%monster%', '%ghost%', '%dead%', '%zombie%', '%undead%'
    ])
  AND f.description NOT ILIKE ANY (ARRAY[
        '%beast%', '%monster%', '%ghost%', '%dead%', '%zombie%', '%undead%'
    ]);

SELECT COUNT(*) AS total_films,
    SUM(length) AS total_minutes,
    ROUND(SUM(length) / 60.0, 2) AS total_hours,
    ROUND(SUM(length) / 60.0 / 24.0, 2) AS total_days
FROM film;


