#CH-1 Display:
-Product
-Price
Create a new column
Price >=500 (Expensive)
Else (Affordable)

USE data_science_journey;

SELECT
    Product,
    Price,
    CASE
        WHEN Price >= 500 THEN 'Expensive'
        ELSE "Affordable"
    END AS Price_Label
FROM sales;

#CH-2 Display:
-Product
-Revenue
Create a label: Revenue_Status
Revenue >= 1000 (HIGH)
ELSE (LOW)

SELECT
    Product,
    Price * Quantity AS Revenue,
    CASE
        WHEN Price * Quantity >= 1000 THEN 'High'
        ELSE 'Low'
    END AS Revenue_Status
FROM sales;

#CH-3 Display:
-Product
-Quantity
Create label: Stock
-Quantity >=5 (HIGH STOCK)
-Quantity >=3 (MEDIUM STOCK)
-ELSE (LOW STOCK)

SELECT
    Product,
    Quantity,
    CASE  
        WHEN Quantity >= 5 THEN 'High Stock'
        WHEN Quantity >= 3 THEN 'Medium Stock'
        ELSE 'Low Stock'
    END AS Stock
FROM sales;