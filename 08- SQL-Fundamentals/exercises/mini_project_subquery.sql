#miniprojectsubquery

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

SELECT
    Product,
    Category,
    Price,
    Quantity
FROM sales
WHERE Price >
(
    SELECT AVG(Price)
    FROM sales
)
AND Quantity >
(
    SELECT AVG(Quantity)
    FROM sales
)
ORDER BY Price DESC;