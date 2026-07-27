#miniprojectsubquerywithin

🚀 Mini Project

Create a report that displays:

Product
Category
Price
Quantity

But only for products that:

Belong to a category that contains products priced above 500.
Have a minimum quantity of 2.

Sort by highest Price.

-- ===========
-- SQL REPORT
-- ===========

SELECT
    Product,
    Category,
    Price,
    Quantity
FROM sales
WHERE Category IN
(
    SELECT Category
    FROM sales
    WHERE Price >500
)
AND Quantity >=2
ORDER BY Price DESC;