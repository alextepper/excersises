-- Database: dvdrental

-- SELECT * FROM customer

-- SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;

-- SELECT create_date FROM customer

-- SELECT * from customer ORDER BY first_name DESC

-- SELECT film_id, title, description, release_year FROM film ORDER BY release_year DESC

-- SELECT address, phone FROM address WHERE district = 'Texas'

-- SELECT * from film WHERE film_id = 15 or film_id = 150

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'American Circus'

-- SELECT film_id, title, description, length, rental_rate 
-- FROM film 
-- WHERE title LIKE '%' || SUBSTRING('American Circus', 1, 2) || '%'

-- SELECT * FROM film ORDER BY rental_rate, replacement_cost LIMIT 10

-- SELECT * FROM film ORDER BY rental_rate, replacement_cost FETCH FIRST 10 ROWS ONLY OFFSET 10 

-- SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- FROM customer
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id

-- SELECT film.title
-- from film
-- where film.film_id not in (select film_id from inventory)

-- SELECT city.city, country.country
-- FROM city
-- INNER JOIN country
-- ON city.country_id = country.country_id
-- ORDER BY country.country

-- SELECT customer.customer_id, customer.first_name || ' ' || customer. last_name, payment. amount, payment. payment_date
-- FROM customer 
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id
-- ORDER BY payment.staff_id