USE data_science_journey;

#CH-1 - Challenge 1
Display
OrderID
ProductName
Quantity
using RIGHT JOIN.

SELECT 
    o.OrderID, 
    p.ProductName, 
    o.Quantity
FROM products p
RIGHT JOIN orders o
ON p.ProductID = o.ProductID;

#Challenge 2
Use IFNULL() so that a NULL value for ProductName is replaced with:
Unknown Product
(Hint: IFNULL(p.ProductName, 'Unknown Product'))

SELECT
    o.OrderID,
    IFNULL(p.ProductName, 'Unknown Product') AS ProductName,
    o.Quantity
FROM products p
RIGHT JOIN orders o
ON p.ProductID = o.ProductID;

#Challenge 3
Display
OrderID
ProductName
Quantity
Revenue
If ProductName is not found, still display its OrderID.

SELECT
    o.OrderID,
    IFNULL(p.ProductName, 'Unknown Product') AS ProductName,
    IFNULL(o.Quantity,0) AS Quantity,
    p.Price * IFNULL(o.Quantity,0) AS Revenue
FROM products p
RIGHT JOIN orders o
ON p.ProductID = o.ProductID;