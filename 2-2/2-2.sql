SELECT first_name, last_name, item, amount
FROM Customers
INNER JOIN Orders
ON Customers.customer_id = Orders.customer_id
