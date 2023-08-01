-- Database: day3DB

-- create table book(
-- 	book_id serial primary key,
-- 	title varchar(50) not null,
-- 	author varchar(50) not null
-- )

-- insert into book(title, author)
-- values
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee')

-- create table student(
-- 	student_id serial primary key,
-- 	name varchar(30) not null unique,
-- 	age integer check (age <= 15)
-- )

-- insert into student(name, age)
-- values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14)

-- create table library(
-- 	book_fk_id integer references book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	student_fk_id integer references student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	borrowed_date date not null
-- )

-- insert into library(book_fk_id, student_fk_id, borrowed_date)
-- values
-- ((select book_id from book where title = 'Alice In Wonderland'),
--  (select student_id from student where name = 'John'),
-- '2022-02-15'),
-- ((select book_id from book where title = 'To kill a mockingbird'),
--  (select student_id from student where name = 'Bob'),
-- '2021-03-03'),
-- ((select book_id from book where title = 'Alice In Wonderland'),
--  (select student_id from student where name = 'Lera'),
-- '2021-05-23'),
-- ((select book_id from book where title = 'Harry Potter'),
--  (select student_id from student where name = 'Bob'),
-- '2021-08-12')

-- select * from library

-- select 
-- 	(select name from student where student_id = student_fk_id),
--  	(select title from book where book_id = book_fk_id),
-- 	borrowed_date
-- from library

-- select 
-- 	avg((select age from student where student_id = student_fk_id))
-- from library
-- where book_fk_id in (select book_id from book where book_id = book_fk_id)

-- DELETE FROM student
-- WHERE student_id = 1;

-- select * from library