#CH1-Calculate the total quantity sold.
USE data_science_journey;

SELECT
    SUM(Quantity) AS Total_Quantity
FROM sales;