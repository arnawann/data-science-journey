USE data_science_journey;

#ch1-Display:
Product
Price
Quantity
Revenue
(Calculate Revenue using Price * Quantity.)

SELECT
    Product,
    Price,
    Quantity,
    Price * Quantity AS Revenue
FROM sales;

#ch2-Display:
-Product
-Category 
in a single column using CONCAT().

SELECT
    CONCAT(Product, ' - ', Category) AS Product_Info
FROM sales;

#ch3-Display categories that have more than 2 products.
Display the average price for each category with two decimal places.
Use ROUND().

SELECT
    Category,
    ROUND(AVG(Price),2) AS Average_Price
FROM sales
GROUP BY Category;