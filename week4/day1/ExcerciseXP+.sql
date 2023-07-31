-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE TABLE students (
-- 	students_id SERIAL PRIMARY KEY,
--  	first_name VARCHAR (50) NOT NULL,
--  	last_name VARCHAR (100) NOT NULL,
-- 	birth_date DATE NOT NULL
-- )

-- INSERT INTO students (first_name, last_name, birth_date)
-- VALUES
-- 	('Marc','Benichou','1998-11-02'),
-- 	('Yoan','Cohen','2010-12-03'),
-- 	('Lea','Benichou','1987-07-27'),
-- 	('Amelia','Dux','1996-04-07'),
-- 	('David','Grez','2003-06-14'),
-- 	('Omer','Simpson','1980-10-03')
-- 	;

-- SELECT first_name, last_name FROM students;


-- SELECT * FROM students WHERE students_id = 2

-- SELECT * FROM students WHERE last_name = 'Benichou' and first_name = 'Marc'

-- SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'

-- SELECT * FROM students WHERE first_name LIKE '%a%'

-- SELECT * FROM students WHERE first_name LIKE 'A%'

-- SELECT * FROM students WHERE first_name LIKE '%a'

-- SELECT * FROM students WHERE SUBSTRING(first_name, 2) LIKE '%a%';

-- SELECT * FROM students WHERE students_id = 2 OR students_id = 3

-- SELECT * FROM students WHERE date_part('year', birth_date) >= '2000'

