#miniprojectaliasesandcalculatedcolumns

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

SELECT
    Category,
    Product,
    Price,
    Quantity,
    Price * Quantity AS Revenue
FROM sales
WHERE ROUND(Revenue,2);

SELECT
    Product,
    Category,
    Price,
    Quantity,
    Price * Quantity AS Revenue,
    ROUND(Price * Quantity,2) AS Rounded_Revenue
FROM sales
ORDER BY Revenue DESC;