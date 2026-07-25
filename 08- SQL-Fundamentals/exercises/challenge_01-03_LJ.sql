USE data_science_journey;

#CH-1 - Challenge 1
Display
ProductName
Category
Quantity
using a LEFT JOIN.

SELECT 
    p.ProductName, 
    p.Category, 
    o.Quantity
FROM products p
LEFT JOIN orders o
ON p.ProductID = o.ProductID;

#Challenge 2
Display
ProductName
Quantity
But if Quantity is NULL, display 0.

SELECT
    p.ProductName,
    IFNULL(o.Quantity,0) AS Quantity
FROM products p
LEFT JOIN orders o
ON p.ProductID = o.ProductID;

#Challenge 3
Display
ProductName
Price
Quantity
Revenue
Use a LEFT JOIN.
If Quantity is NULL, treat it as 0.

SELECT
    p.ProductName,
    p.Price,
    IFNULL(o.Quantity,0) AS Quantity,
    p.Price * IFNULL(o.Quantity,0) AS Revenue
FROM products p
LEFT JOIN orders o
ON p.ProductID = o.ProductID;