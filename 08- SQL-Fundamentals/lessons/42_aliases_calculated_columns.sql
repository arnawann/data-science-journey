USE data_science_journey;

#42- alias
SELECT
    AVG(Price) AS Average_Price
FROM sales;

#Aliases can also be used for table names.

SELECT *
FROM sales AS s;

#43- calculated column
#df["Revenue"] = df["Price"] * df["Quantity"]
#Di SQL tidak perlu membuat kolom baru.

SELECT
    Product,
    Price,
    Quantity,
    Price * Quantity AS Revenue
FROM sales;

#44 - CONCAT()

SELECT
    CONCAT(Product, ' - ', Category) AS Product_Info
FROM sales;

#45 - ROUND()
#simplify decimal places

SELECT
    ROUND(AVG(Price), 2) AS Average_Price
FROM sales;

#46 - Combination

SELECT
    Product,
    Category,
    Price,
    Quantity,
    Price * Quantity AS Revenue,
    ROUND(Price * Quantity,2) AS Rounded_Revenue
FROM sales;