#miniprojectmultiplejoin

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

SELECT
    o.OrderID,
    c.CustomerName,
    c.City,
    p.ProductName,
    p.Category,
    p.Price,
    o.Quantity,
    p.Price * o.Quantity AS Revenue
FROM orders o
INNER JOIN customers c
ON o.CustomerID = c.CustomerID
INNER JOIN products p
ON o.ProductID = p.ProductID
ORDER BY Revenue DESC;