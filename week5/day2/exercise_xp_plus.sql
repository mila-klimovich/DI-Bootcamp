-- CREATE TABLE students (
--  student_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (30) NOT NULL,
--  last_name VARCHAR (20) NOT NULL,
--  birth_date date 
-- )

-- INSERT INTO students (first_name, last_name, birth_date)
-- VALUES
-- 	('Marc', 'Benichou', '02/11/1998'),
-- 	('Yoan', 'Cohen', '03/12/2010'),
-- 	('Lea', 'Benichou', '27/07/1987'),
-- 	('Amelia', 'Dux', '07/04/1996'),
-- 	('David', 'Grez', '14/06/2003'),
-- 	('Omer', 'Simpson', '03/10/1980')

-- INSERT INTO students (last_name, first_name, birth_date)
-- VALUES 
-- 	('Klimovich', 'Mila', '28/10/1989')
	
-- SELECT 
-- 	first_name,
-- 	last_name
-- FROM
-- 	students

SELECT first_name, last_name FROM students WHERE student_id = 2

-- SELECT * FROM students