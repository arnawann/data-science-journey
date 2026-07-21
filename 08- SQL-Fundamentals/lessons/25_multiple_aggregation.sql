USE data_science_journey;

SELECT
    COUNT(*) AS Total_Products,
    SUM(Quantity) AS Total_Quantity,
    AVG(Price) AS Average_Price,
    MAX(Price) AS Highest_Price,
    MIN(Price) AS Lowest_Price
FROM sales;