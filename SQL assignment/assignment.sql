/* customer order between 1 aug to 15 aug */

select count(*),customer_id from payment where payment_date between '2005-08-01 00:00:00' and '2005-08-15 00:00:00'group by customer_id;





/* quantity is greater than 100 */

select customer_id,count(payment_id) as counter from payment group by customer_id having counter > 35;




/*  find customer products  */

SELECT customer.customer_id, customer.first_name,customer.last_name, film.title
FROM customer 
INNER JOIN rental
ON customer.customer_id = rental.customer_id
INNER JOIN inventory 
ON rental.inventory_id = inventory.inventory_id
INNER JOIN film 
ON inventory.film_id = film.film_id
ORDER BY customer.customer_id;



/* write a query to fetch total price of all the products order by each customer */

SELECT concat(customer.first_name, ' ' ,customer.last_name) AS customer_name, 
sum(payment.amount) AS Total_price
FROM payment
JOIN customer
ON customer.customer_id = payment.customer_id
GROUP BY payment.customer_id;











