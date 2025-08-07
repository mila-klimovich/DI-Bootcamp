-- Sample data
-- CREATE TABLE sample_data (id INT, value INT);
-- INSERT INTO sample_data (id, value) VALUES (1, 10), (2, NULL), (3, 30);

-- SELECT * FROM sample_data

-- SELECT id, COALESCE(value, 20) FROM sample_data

-- UPDATE sample_data
-- SET value = (SELECT MIN(value) FROM sample_data WHERE value = 20)
-- WHERE value = 20

-- SELECT * FROM sample_data

-- UPDATE sample_data
-- SET value = (SELECT MIN(value) FROM sample_data WHERE value IS NOT NULL)
-- WHERE value IS NULL

-- SELECT * FROM sample_data

-- SELECT id, value, COUNT(*)
-- FROM sample_data
-- GROUP BY id, value
-- HAVING COUNT(*) > 1;

-- CREATE TABLE sample_data2 (id INT, value VARCHAR(50));
-- INSERT INTO sample_data2 (id, value) VALUES (1, 'apple'), (2, 'Apple'), (3, 'APPLE');

-- UPDATE sample_data2
-- SET value = 'APPLE'
-- WHERE UPPER(value) = 'APPLE'

-- SELECT * FROM sample_data2

-- CREATE TABLE patients (
--     patient_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     date_of_birth DATE
-- );
-- -- Create Visits Table (2nd Normal Form, normalized from the patient data)
-- CREATE TABLE visits (
--     visit_id SERIAL PRIMARY KEY,
--     patient_id INT REFERENCES patients(patient_id),
--     visit_date DATE,
--     diagnosis VARCHAR(100)
-- );

-- Insert data into patients table
-- INSERT INTO patients (first_name, last_name, date_of_birth)
-- VALUES
--     ('John', 'Doe', '1985-02-20'),
--     ('Jane', 'Smith', '1990-05-15'),
--     ('Emily', 'Johnson', '1982-08-25');
-- -- Insert data into visits table
-- INSERT INTO visits (patient_id, visit_date, diagnosis)
-- VALUES
--     (1, '2024-01-10', 'Flu'),
--     (1, '2024-02-20', 'Cold'),
--     (2, '2024-03-05', 'Headache'),
--     (3, '2024-04-10', 'Diabetes');

-- CREATE TABLE denormalized_patients_visits AS
-- (
-- SELECT first_name, last_name, date_of_birth, v.patient_id, visit_date, diagnosis
-- FROM patients p
-- JOIN visits v ON p.patient_id = v.patient_id
-- )

-- SELECT * FROM denormalized_patients_visits

-- CREATE TABLE sales_data_new (
--     product_id INT,
--     category VARCHAR(50),
--     sales INT
-- );
-- INSERT INTO sales_data_new (product_id, category, sales) VALUES
-- (1, 'Electronics', 100),
-- (1, 'Clothing', 50),
-- (1, 'Groceries', 30),
-- (2, 'Electronics', 200),
-- (2, 'Clothing', 70),
-- (2, 'Groceries', 60),
-- (3, 'Electronics', 150),
-- (3, 'Clothing', 90),
-- (3, 'Groceries', 40);

-- SELECT *
-- FROM (
--     SELECT product_id, category, sales
--     FROM sales_data
-- ) AS SourceTable
-- PIVOT (
--     SUM(sales)
--     FOR category IN ([Electronics], [Clothing], [Groceries])
-- ) AS PivotTable;

-- SELECT product_id, 
-- SUM(CASE WHEN category = 'Electronics' THEN sales ELSE 0 END) AS Electronics,
-- SUM(CASE WHEN category = 'Clothing' THEN sales ELSE 0 END) AS Clothing,
-- SUM(CASE WHEN category = 'Groceries' THEN sales ELSE 0 END) AS Groceries
-- FROM sales_data_new
-- GROUP BY product_id

-- SELECT category, SUM(sales)
-- FROM sales_data_new
-- GROUP BY category

-- CREATE TABLE users (
--     id INT PRIMARY KEY,
--     status VARCHAR(10)
-- );
-- INSERT INTO users (id, status)
-- VALUES
-- (1, 'A'),
-- (2, 'I'),
-- (3, 'X2'),  -- Invalid status
-- (4, 'I'),
-- (5, Null),  -- Invalid status
-- (6, 'Z');  -- Invalid status

-- UPDATE users
-- SET status = CASE WHEN status = 'A' THEN 'Active'
-- 	WHEN status = 'I' THEN 'Inactive'
-- 	ELSE 'Unknown'
-- 	END

-- SELECT
-- 	id,
-- CASE WHEN status = 'A' THEN 'Active'
-- 	WHEN status = 'I' THEN 'Inactive'
-- 	ELSE 'Unknown'
-- 	END
-- FROM users

-- SELECT *  FROM users;

-- CREATE TABLE exercise_data (
--     id INT,
--     date VARCHAR(50),
--     value INT,
--     status VARCHAR(1)
-- );

-- INSERT INTO exercise_data (id, date, value, status) VALUES
-- (1, '2021-01-01', 10, 'A'),
-- (2, '2021-01-02', NULL, 'I'),
-- (3, '2021-01-03', -5, 'A'),
-- (4, '2021-01-04', 20, 'X');

-- SELECT * FROM exercise_data

-- SELECT
-- id,
-- CASE
-- 	WHEN status = 'A' THEN 'Active'
-- 	WHEN status = 'I' THEN 'Inactive'
-- 	ELSE 'Unknown' END as status
-- FROM exercise_data

-- UPDATE exercise_data
-- SET date = REGEXP_REPLACE(date, '-', '/')

-- SELECT * FROM exercise_data

-- UPDATE exercise_data
-- SET value = value * (-1) + 1
-- WHERE value < 0

-- DELETE FROM exercise_data WHERE value <= 0 OR value IS NULL

-- SELECT * FROM exercise_data

-- ALTER TABLE exercise_data
-- ADD CONSTRAINT positive_value_check CHECK (value > 0)

-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     name VARCHAR(50),
--     department_id INT
-- );
-- CREATE TABLE departments (
--     department_id INT PRIMARY KEY,
--     department_name VARCHAR(50)
-- );
-- INSERT INTO employees (employee_id, name, department_id)
-- VALUES
-- (1, 'Alice', 1),
-- (2, 'Bob', 2),
-- (3, 'Charlie', 5),
-- (4, 'David', 3),
-- (5, 'Sam', 1),
-- (6, 'David', 3);
-- INSERT INTO departments (department_id, department_name)
-- VALUES
-- -- (4, 'Marketing'),
-- (1, 'R&D'),
-- (7, 'HR');

-- SELECT employee_id, name, d.department_id, department_name
-- FROM employees e
-- CROSS JOIN departments d --ON e.department_id = d.department_id