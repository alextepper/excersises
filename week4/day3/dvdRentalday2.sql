-- Database: dvdrental

-- select name from language

-- select film.title, film.description, language.name
-- from film
-- left join language
-- on film.language_id = language.language_id
-- order by language.language_id

-- select film.title, film.description, language.name
-- from film
-- right join language
-- on film.language_id = language.language_id
-- order by language.language_id

-- create table new_film(
-- 	id serial primary key,
-- 	name varchar(100) not null
-- )

-- insert into new_film(name)
-- values 
-- ('Saving, Private Dancer'),
-- ('Closenheimer'),
-- ('Kenby')

-- create table customer_review(
-- 	review_id serial primary key,
-- 	customer_id int references customer(customer_id) on delete cascade on update cascade,
-- 	film_id int references new_film(id) on delete cascade on update cascade,
-- 	language_id int references language(language_id),
-- 	title varchar(50) not null,
-- 	score int check(score between 1 and 10),
-- 	review_text text not null,
-- 	last_update timestamp not null
-- )

-- insert into customer_review(customer_id, film_id, language_id, title, score,review_text,last_update)
-- values(23, 1, 1, 'stupid soap opera', 3, 'very stupid', now():: timestamp)


-- delete from new_film
-- where id = 1

-- select * from customer_review

-- update film set language_id = 3 where title like '%Hope%'

-- select * from film 
-- where language_id = 3

-- drop table customer_review

-- select count(*) 
-- from rental 
-- where return_date is null

-- select title, replacement_cost
-- from film 
-- where film_id in
-- 	(select film_id 
-- 	from inventory
-- 	where inventory_id in
-- 		(select inventory_id  
-- 		from rental 
-- 		where return_date is null))
-- order by replacement_cost desc
-- limit 30

-- select * 
-- from film 
-- where fulltext @@ tsquery('sumo') and
-- film_id in (
-- 	select film_id 
-- 	from film_actor 
-- 	where actor_id = (
-- 		select actor_id 
-- 		from actor 
-- 		where first_name = 'Penelope' and last_name = 'Monroe'))

-- select * 
-- from film 
-- where length < 60
-- and rating = 'R'
-- and film_id in (select film_id 
-- 				from film_category 
-- 				where category_id 
-- 				in (select category_id
-- 					from category
-- 					where name = 'Documentary'))

-- select * 
-- from film
-- where film_id in (select film_id
-- 				from inventory
-- 				where inventory_id in (
-- 					select inventory_id 
-- 					from rental 
-- 					where rental_id in (select rental_id 
-- 										from payment 
-- 										where amount > 4.00)
-- 					and return_date between '2005-07-28' and '2005-08-01'
-- 					and customer_id in (select customer_id 
-- 										  from customer 
-- 										  where first_name = 'Matthew' 
-- 										  and last_name = 'Mahan')))
	
-- select *
-- from film f
-- inner join inventory i
-- on f.film_id = i.film_id
-- inner join rental r
-- on i.inventory_id = r.inventory_id
-- inner join customer c
-- on r.customer_id = c.customer_id
-- where c.first_name = 'Matthew' and c.last_name = 'Mahan'
-- and f.description like '%Boat'
											  

