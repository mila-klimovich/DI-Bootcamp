SELECT DISTINCT f.film_id, f.title, f.rating
FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE f.rating IN ('G', 'PG')
  AND (r.return_date IS NOT NULL OR r.rental_id IS NULL);

CREATE TABLE waiting_list_children (
    waiting_id SERIAL PRIMARY KEY,
    child_name VARCHAR(100) NOT NULL,
    film_id INT NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES film(film_id)
);

SELECT f.film_id, f.title, COUNT(w.waiting_id) AS number_waiting
FROM waiting_list_children w
JOIN film f ON w.film_id = f.film_id
GROUP BY f.film_id, f.title
ORDER BY number_waiting DESC;

INSERT INTO waiting_list_children (child_name, film_id)
VALUES 
    ('Alice', 12),
    ('Bob', 12),
    ('Charlie', 25),
    ('Daisy', 12);

