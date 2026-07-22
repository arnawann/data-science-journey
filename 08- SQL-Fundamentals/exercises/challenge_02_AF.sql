#CH2-Find the average price of all products.
USE data_science_journey;

SELECT
    AVG(Price) AS Average_Price
FROM sales;