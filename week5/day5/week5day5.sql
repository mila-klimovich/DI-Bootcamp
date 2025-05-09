CREATE TABLE employees (
    employeeID INT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    quality VARCHAR(50)
);

CREATE TABLE ratings (
    ratingID INT PRIMARY KEY,
    employeeID INT,
    rating INT,
    FOREIGN KEY (employeeID) REFERENCES employees(employeeID)
);

INSERT INTO employees (employeeID, firstname, lastname, quality) VALUES
(1, 'Alice', 'Smith', 'Integrity'),
(2, 'Bob', 'Johnson', 'Creativity'),
(3, 'Charlie', 'Lee', 'Punctuality'),
(4, 'Dana', 'White', 'Teamwork');

INSERT INTO ratings (ratingID, employeeID, rating) VALUES
(1, 1, 4),
(2, 2, 2),
(3, 3, 5),
(4, 4, 3);

select * FROM ratings
SELECT employees.employeeID, employees.firstname, employees.lastname, ratings.rating  
FROM employees AS A
JOIN ratings AS B ON  A.employeeID = ratings.employeeID  
WHERE B.rating > 3;

SELECT A.employeeID, A.firstname, A.lastname, B.rating  
FROM employees AS A
JOIN ratings AS B ON  A.employeeID = B.employeeID  
WHERE B.rating > (SELECT AVG(rating) FROM ratings);

______________________

Parent table: colors
CREATE TABLE colors (
    color_id SERIAL PRIMARY KEY,
    name TEXT
);

Child table: cars with ON DELETE RESTRICT
CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    car_color INTEGER REFERENCES colors(color_id) ON DELETE RESTRICT,
    car_name TEXT
);

Insert into colors
INSERT INTO colors (name) VALUES
('red'),
('blue'),
('yellow'),
('pink');

Insert into cars
INSERT INTO cars (car_color, car_name) VALUES
(1, 'Ferrari'),
(2, 'Ford'),
(3, 'BMW'),      -- yellow
(4, 'Bugatti');  -- pink

SELECT * FROM cars

DELETE FROM colors WHERE name = 'yellow';

DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    car_color INTEGER REFERENCES colors(color_id) ON DELETE CASCADE,
    car_name TEXT
);

INSERT INTO cars (car_color, car_name) VALUES
(1, 'Ferrari'),
(2, 'Ford'),
(3, 'BMW'),      -- yellow
(5, 'Bugatti');  -- pink

DELETE FROM colors WHERE name = 'pink';

SELECT * FROM colors

INSERT INTO colors (name) VALUES
('pink');

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(50)
);

CREATE TABLE addresses (
  user_id INTEGER PRIMARY KEY,
  city VARCHAR(50),
  street VARCHAR(100),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (name) VALUES ('Alice'), ('Bob');
INSERT INTO addresses (user_id, city, street) VALUES
(1, 'New York', '5th Avenue'),
(2, 'Los Angeles', 'Sunset Blvd');


SELECT u.name, a.city, a.street
FROM users u
INNER JOIN addresses a ON u.user_id = a.user_id;

CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  customer_name VARCHAR(50)
);

CREATE TABLE items (
  item_id SERIAL PRIMARY KEY,
  item_name VARCHAR(50)
);

CREATE TABLE order_items (
  order_id INTEGER,
  item_id INTEGER,
  quantity INTEGER,
  PRIMARY KEY (order_id, item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (item_id) REFERENCES items(item_id)
);

INSERT INTO orders (customer_name) VALUES ('John'), ('Emma');
INSERT INTO items (item_name) VALUES ('Laptop'), ('Phone'), ('Headphones');

INSERT INTO order_items (order_id, item_id, quantity) VALUES
(1, 1, 1),  -- John ordered 1 Laptop
(1, 3, 2),  -- John ordered 2 Headphones
(2, 2, 1),  -- Emma ordered 1 Phone
(2, 3, 1);  -- Emma ordered 1 Headphones

SELECT o.customer_name, i.item_name, oi.quantity
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN items i ON oi.item_id = i.item_id;