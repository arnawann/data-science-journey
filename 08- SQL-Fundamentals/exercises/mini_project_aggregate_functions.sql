#miniprojectaf
USE data_science_journey;

SELECT
    COUNT(*) AS Total_Product,
    SUM(Quantity) AS Total_Quantity,
    SUM(Price * Quantity) AS Total_Revenue,
    AVG(Price) AS Average_Price,
    MAX(Price) AS Highest_Price,
    MIN(Price) AS Lowest_Price

FROM sales;