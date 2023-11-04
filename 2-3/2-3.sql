SELECT
    Customers.first_name,
    Customers.country,
    Shippings.status
FROM
    Customers JOIN Orders ON Customers.customer_id = Orders.customer_id
			JOIN Shippings ON Orders.customer_id = Shippings.customer
WHERE
    Orders.item = 'Keyboard';
