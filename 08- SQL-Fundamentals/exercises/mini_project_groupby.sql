#miniprojectgroupby

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

SELECT
    Category,
    COUNT(*) AS Total_Product,
    SUM(Quantity) AS Total_Quantity,
    AVG(Price) AS Average_Price,
    MAX(Price) AS Highest_Price,
    MIN(Price) AS Lowest_Price

FROM sales
GROUP BY Category;