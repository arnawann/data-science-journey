USE data_science_journey;

#69-basic case when

SELECT
    Product,
    Price,
    CASE
        WHEN Price > 500 THEN 'Expensive'
        ELSE 'Affordable'
    END AS Price_Label
FROM sales;

#70-A CASE can have many conditions.

SELECT
    Product,
    Price,
    CASE
        WHEN Price >= 1000 THEN 'Premium'
        WHEN Price >= 500 THEN 'High'
        WHEN Price >= 100 THEN 'Medium'
        ELSE 'Low'
    END AS Price_Level
FROM sales;

NB: SQL reads CASE statements from top to bottom.

#71-CASE can also use Revenue.

SELECT
    Product,
    Price,
    Quantity,
    Price * Quantity AS Revenue,
    CASE
        WHEN Price * Quantity >= 1000 THEN 'High Revenue'
        ELSE 'Low Revenue'
    END AS Revenue_Status
FROM sales;

#72-CASE can be used with GROUP BY.

SELECT
    Category,
    AVG(Price) AS Average_Price,
    CASE
        WHEN AVG(Price) >=500 THEN 'Premium Category'
        ELSE 'Regular Category'
    END AS Category_Level
FROM sales
GROUP BY Category;