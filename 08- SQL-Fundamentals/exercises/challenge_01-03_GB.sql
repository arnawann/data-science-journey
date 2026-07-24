#Urutkan produk berdasarkan Category, lalu Quantity tertinggi.
USE data_science_journey;

#Challenge1 Calculate the total quantity for each category.

SELECT
    Category,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category;

#Challenge2 Calculate the average price for each category.

SELECT
    Category,
    AVG(Price) AS Average_Price
FROM sales
GROUP BY Category;

#Challenge 3 Show all productsin the Electronicsor Clothing categories.

SELECT
    Category,
    COUNT(*) AS Total_Product
FROM sales
GROUP BY Category;