USE data_science_journey;

#55-create customers
#Create a customers table

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(100)
);

#56-insert customers
#Enter the data.

INSERT INTO customers VALUES
(1, 'Andi', 'Jakarta'),
(2, 'Budi', 'Bandung'),
(3, 'Citra', 'Surabaya'),
(4, 'Dina', 'Yogyakarta');

#57-Now we need to modify the orders table.
Because now each order needs to specify
which customer made the purchase.
Add a CustomerID column.

ALTER TABLE orders
ADD CustomerID INT;

#Then enter the CustomerID.

UPDATE orders
SET CustomerID = 1
WHERE OrderID = 101;

UPDATE orders
SET CustomerID = 2
WHERE OrderID = 102;

UPDATE orders
SET CustomerID = 3
WHERE OrderID = 103;

UPDATE orders
SET CustomerID = 4
WHERE OrderID = 104;

UPDATE orders
SET CustomerID = 1
WHERE OrderID = 105;

#Now take a look at the results:

SELECT * FROM orders;

#58-join 3 table

SELECT
    c.CustomerName,
    p.ProductName,
    o.Quantity
FROM orders o
INNER JOIN customers c
ON o.CustomerID = c.CustomerID
INNER JOIN products p
ON o.ProductID = p.ProductID;

#59-Add revenue

SELECT
    c.CustomerName,
    p.ProductName,
    p.Price,
    o.Quantity,
    p.Price * o.Quantity AS Revenue
FROM orders o
INNER JOIN customers c
ON o.CustomerID = c.CustomerID
INNER JOIN products p
ON o.ProductID = p.ProductID;
