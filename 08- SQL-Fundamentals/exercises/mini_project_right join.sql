#miniprojectrightjoin

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

SELECT
    o.OrderID,
    IFNULL(p.ProductName, 'Unknown Product') AS ProductName,
    p.Category,
    p.Price,
    IFNULL (o.Quantity,0) AS Quantity,
    p.Price * IFNULL(o.Quantity,0) AS Revenue
FROM products p
RIGHT JOIN orders o
ON p.ProductID = o.ProductID;
ORDER BY o.OrderID;