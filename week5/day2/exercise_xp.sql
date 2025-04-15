CREATE TABLE items (
 item_id SERIAL PRIMARY KEY,
 item_name VARCHAR (20) NOT NULL,
 price SMALLINT NOT NULL
)

INSERT INTO items (item_name, price)
VALUES
	('Small Desk', 100),
	('Large Desk', 300),
	('Fan', 80)

CREATE TABLE customers(
 customer_id SERIAL PRIMARY KEY,
 customer_name VARCHAR (20) NOT NULL,
 customer_last_name VARCHAR (30) NOT NULL
)

INSERT INTO customers (customer_name, customer_last_name)
VALUES
	('Greg', 'Jones'),
	('Sandra', 'Jones'),
	('Scott', 'Scott'),
	('Trevor', 'Green'),
	('Melanie', 'Johnson')

SELECT * FROM customers

SELECT * FROM items
SELECT * FROM items WHERE price > 80
SELECT * FROM items WHERE price <= 300
SELECT * FROM customers WHERE customer_last_name = 'Smith'
SELECT * FROM customers WHERE customer_last_name = 'Jones'
SELECT * FROM customers WHERE customer_name != 'Scott'


