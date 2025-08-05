-- CREATE TABLE employees (
--     department_id INT,
--     employee_id INT,
--     salary INT
-- );
-- INSERT INTO employees (department_id, employee_id, salary) VALUES
-- (1, 101, 80000),
-- (1, 102, 75000),
-- (1, 103, 75000),
-- (1, 104, 60000),
-- (2, 201, 90000),
-- (2, 202, 90000),
-- (2, 203, 85000),
-- (2, 204, 80000);

-- SELECT employee_id, salary, department_id,
-- SUM(salary) OVER(PARTITION BY department_id) AS total_salary_by_department
-- FROM employees

-- SELECT department_id, employee_id, salary,
-- ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_number
-- FROM employees

-- SELECT department_id, employee_id, salary,
-- ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_number,
-- RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
-- FROM employees

-- SELECT department_id, employee_id, salary,
-- ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_number,
-- RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank,
-- DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
-- FROM employees

-- SELECT employee_id, department_id, salary,
--        NTILE(3) OVER (PARTITION BY department_id ORDER BY salary DESC) AS quartile
-- FROM employees;

-- CREATE TABLE employees_new (
--     employee_id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     department_id INT,
--     salary DECIMAL(10, 2)
-- );

-- CREATE TABLE sales_data (
--     sale_id INT PRIMARY KEY,
--     employee_id INT,
--     sales DECIMAL(10, 2),
--     FOREIGN KEY (employee_id) REFERENCES employees_new(employee_id)
-- );

-- INSERT INTO employees_new (employee_id, first_name, last_name, department_id, salary) VALUES
-- (1, 'John', 'Doe', 1, 60000),
-- (2, 'Jane', 'Smith', 2, 80000),
-- (3, 'Jim', 'Brown', 3, 90000),
-- (4, 'Jake', 'White', 4, 70000),
-- (5, 'Jill', 'Green', 5, 75000),
-- (6, 'Jack', 'Black', 3, 95000),
-- (7, 'Jerry', 'Gray', 2, 82000),
-- (8, 'Jim', 'Black', 3, 90000),
-- (9, 'Julia', 'Smith', 2, 80000);

-- INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
-- (1, 1, 1000),
-- (2, 2, 1500),
-- (3, 3, 2000),
-- (4, 4, 700),
-- (5, 5, 1300),
-- (6, 6, 1750),
-- (7, 7, 1200),
-- (8, 8, 2000),
-- (9, 9, 1200);

-- SELECT * FROM sales_data
-- SELECT * FROM employees_new

-- SELECT department_id, first_name, last_name, salary,
-- ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_number
-- FROM employees_new

-- SELECT e.employee_id, e.salary, department_id, d.sales,
-- SUM(d.sales) OVER(ORDER BY d.employee_id) AS running_total_sales
-- FROM employees_new e
-- JOIN sales_data d ON e.employee_id = d.employee_id

-- SELECT e.employee_id, e.salary, department_id, d.sales,
-- SUM(d.sales) OVER(PARTITION BY department_id ORDER BY d.employee_id) AS running_total_sales
-- FROM employees_new e
-- JOIN sales_data d ON e.employee_id = d.employee_id

-- CREATE TABLE employees_history (
--     employee_id INT,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     salary NUMERIC(10, 2),
--     department_id INT,
--     MONTH VARCHAR(20),
--     PRIMARY KEY (employee_id, month)
-- );

-- -- Insert data into the employees table with consistent employee_id and monthly salary variations
-- INSERT INTO employees_history (employee_id, first_name, last_name, salary, department_id, month) VALUES
-- -- Department 1: John Doe
-- (1, 'John', 'Doe', 60000, 1, 'January'),
-- (1, 'John', 'Doe', 61000, 1, 'February'),
-- (1, 'John', 'Doe', 60500, 1, 'March'),
-- -- Department 1: Jane Smith
-- (2, 'Jane', 'Smith', 80000, 1, 'January'),
-- (2, 'Jane', 'Smith', 82000, 1, 'February'),
-- (2, 'Jane', 'Smith', 81500, 1, 'March'),
-- -- Department 1: Jerry Gray
-- (3, 'Jerry', 'Gray', 82000, 1, 'January'),
-- (3, 'Jerry', 'Gray', 83000, 1, 'February'),
-- (3, 'Jerry', 'Gray', 82500, 1, 'March'),
-- -- Department 2: Jim Brown
-- (4, 'Jim', 'Brown', 90000, 2, 'January'),
-- (4, 'Jim', 'Brown', 91000, 2, 'February'),
-- (4, 'Jim', 'Brown', 90500, 2, 'March'),
-- -- Department 2: Jack Black
-- (5, 'Jack', 'Black', 95000, 2, 'January'),
-- (5, 'Jack', 'Black', 96000, 2, 'February'),
-- (5, 'Jack', 'Black', 95500, 2, 'March'),
-- -- Department 3: Jake White
-- (6, 'Jake', 'White', 70000, 3, 'January'),
-- (6, 'Jake', 'White', 71000, 3, 'February'),
-- (6, 'Jake', 'White', 70500, 3, 'March'),
-- -- Department 3: Jill Green
-- (7, 'Jill', 'Green', 75000, 3, 'January'),
-- (7, 'Jill', 'Green', 76000, 3, 'February'),
-- (7, 'Jill', 'Green', 75500, 3, 'March');

-- SELECT employee_id, first_name, last_name, department_id, salary,
-- MAX(salary) OVER (PARTITION BY employee_id) as max_salary,
-- MIN(salary) OVER (PARTITION BY employee_id) as min_salary,
-- AVG(salary) OVER (PARTITION BY employee_id) as avg_salary,
-- SUM(salary) OVER (PARTITION BY employee_id) as sum_salary
-- FROM employees_history

-- SELECT employee_id, first_name, last_name, salary, month,
-- 	LEAD(salary, 1) OVER (PARTITION BY employee_id ORDER BY salary) AS next_salary
-- FROM employees_history

-- SELECT employee_id, first_name, last_name, salary, month,
-- 	LEAD(salary, 1) OVER (PARTITION BY employee_id ORDER BY month) AS next_salary,
-- 	LAG(salary, 1) OVER (PARTITION BY employee_id ORDER BY month) AS previous_salary
-- FROM employees_history

-- SELECT employee_id, first_name, last_name, salary,
--        LAST_VALUE(salary) OVER (PARTITION BY employee_id ORDER BY salary) AS last_salary
-- FROM employees_history;

-- SELECT employee_id, first_name, last_name, salary,
--        LAST_VALUE(salary) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_salary
-- FROM employees_history;


-- SELECT employee_id, first_name, last_name, salary,
--        LAST_VALUE(salary) OVER (PARTITION BY employee_id ORDER BY salary ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS last_salary
-- FROM employees_history;


-- SELECT employee_id, first_name, last_name, salary,
--        SUM(salary) OVER (PARTITION BY employee_id ORDER BY salary ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS sum_salary
-- FROM employees_history;

SELECT employee_id, first_name, last_name, salary,
       SUM(salary) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_sum
FROM employees_history;