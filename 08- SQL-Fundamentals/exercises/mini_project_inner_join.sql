#miniprojectinnerjoin
Create a sales report that displays:
OrderID
ProductName
Category
Price
Quantity
Revenue
Then sort by Revenue, starting with the highest.

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;
SELECT
    o.OrderID,
    p.ProductName,
    p.Category,
    p.Price,
    o.Quantity,
    p.Price * o.Quantity AS Revenue
FROM products p
INNER JOIN orders o
ON p.ProductID = o.ProductID
ORDER BY Revenue DESC;

