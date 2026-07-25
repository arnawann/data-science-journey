#miniprojectleftjoin

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

SELECT
    p.ProductName,
    p.Category,
    p.Price,
    IFNULL(o.Quantity,0) AS Revenue
FROM products p
LEFT JOIN orders o
ON p.ProductID = o.ProductID
ORDER BY Revenue DESC;