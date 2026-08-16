-- Write your query below
SELECT c.name
FROM customers c
LEFT JOIN orders
    ON c.id = orders.customer_id
WHERE orders.id IS NULL;


