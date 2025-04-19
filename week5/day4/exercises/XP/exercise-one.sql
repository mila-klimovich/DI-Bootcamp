SELECT * FROM items ORDER BY price ASC
SELECT * FROM items WHERE price >= 80 ORDER BY price DESC

SELECT customer_name, customer_last_name FROM customers ORDER BY customer_name ASC LIMIT 3
SELECT customer_last_name FROM customers ORDER BY customer_last_name DESC