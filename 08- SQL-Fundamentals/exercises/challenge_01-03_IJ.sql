#ch1- Display
ProductName
Category
Quantity
using an INNER JOIN.

SELECT
    p.ProductName,
    p.Category,
    o.Quantity
FROM products p
INNER JOIN orders o
ON p.ProductID = o.ProductID;

#ch2- Display
ProductName
Price
Quantity
Revenue

SELECT
    p.ProductName,
    p.Price,
    o.Quantity,
    p.Price * o.Quantity AS Revenue
FROM products p
INNER JOIN orders o
ON p.ProductID = o.ProductID;

#ch3- Sort the JOIN results by highest Revenue.
(Hint: Use ORDER BY.)

SELECT
    MAX(results) as highest_revenue
FROM sales
ORDER BY highest_revenue DESC;

SELECT
    p.ProductName,
    p.Price,
    o.Quantity,
    p.Price * o.Quantity AS Revenue
FROM products p
INNER JOIN orders o
ON p.ProductID = o.ProductID
ORDER BY Revenue DESC;