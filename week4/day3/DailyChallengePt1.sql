-- Database: day3DB

-- reate table customer(
-- 	customer_id serial primary key,
-- 	first_name varchar(50) not null,
-- 	last_name varchar(50) not null
-- )

-- create table customer_profile(
-- 	profile_id serial primary key,
-- 	isLoggedIn bool default false,
-- 	customer_id integer,
-- 	foreign key(customer_id)
-- 	references customer (customer_id)
-- )

-- insert into customer_profile(first_name, last_name)
-- values ('John', 'Doe'),
--  ('Jerome', 'Lalu'),
--  ('Lea', 'Rive');

-- insert into customer_profile(isLoggedIn, customer_id)
-- values (true, (select customer_id from customer where first_name = 'John'))

-- insert into customer_profile(isLoggedIn, customer_id)
-- values (false, (select customer_id from customer where first_name = 'Jerome'))

-- select first_name 
-- from customer d
-- inner join customer_profile b
-- on d.customer_id = b.customer_id
-- where b.isloggedin = true

-- select d.first_name, b.isloggedin
-- from customer d
-- left join customer_profile b
-- on d.customer_id = b.customer_id

-- select count(*)
-- from customer
-- where customer_id 
-- in (select customer_id from customer_profile where isloggedin is false)