USE data_science_journey;

#ch1-Show categories with a total quantity greater than 10.
SELECT
    Category,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category
HAVING SUM(Quantity) > 10;

#ch2-Show categories with an average price greater than 100.
SELECT
    Category,
    AVG(Price) AS Average_Price
FROM sales
GROUP BY Category
HAVING AVG(Price) > 100;

#ch3-Display categories that have more than 2 products.
SELECT
    Category,
    COUNT(*) AS Total_Product
FROM sales
GROUP BY Category
HAVING COUNT(*) > 2;