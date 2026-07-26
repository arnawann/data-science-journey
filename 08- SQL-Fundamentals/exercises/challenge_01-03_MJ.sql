USE data_science_journey;
MULTIPLE JOIN

#CH-1 - Challenge 1
Display
CustomerName
ProductName
Quantity

SELECT
    c.CustomerName,
    p.ProductName,
    o.Quantity
FROM orders o
INNER JOIN customers c
ON o.CustomerID = c.CustomerID
INNER JOIN products p
ON o.ProductID = p.ProductID;

#Challenge 2
CustomerName
City
ProductName
Price   
    
SELECT
    c.CustomerName,
    c.City,
    p.ProductName,
    p.Price
FROM orders o
INNER JOIN customers c
ON o.CustomerID = c.CustomerID
INNER JOIN products p
ON o.ProductID = p.ProductID;

#Challenge 3
CustomerName
ProductName
Quantity
Revenue
Sort by highest revenue.

SELECT
    c.CustomerName,
    p.ProductName,
    o.Quantity,
    p.Price * o.Quantity AS Revenue
FROM orders o
INNER JOIN customers c
ON o.CustomerID = c.CustomerID
INNER JOIN products p
ON o.ProductID = p.ProductID
ORDER BY Revenue DESC;