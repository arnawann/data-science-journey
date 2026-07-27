USE data_science_journey;

#67-orderofexecution

SELECT 
    Product,
    Price
FROM sales
WHERE Price > 100
ORDER BY Price DESC
LIMIT 2;

#68-Why is this an error?
SELECT
    Product,
    Price * Quantity AS Revenue
FROM sales
WHERE Revenue > 500;

#The answer:
Because when the WHERE clause is executed...
SQL hasn't created the Revenue table yet.
The Revenue table is only created during the
SELECT
But the WHERE clause is executed before the SELECT.
That's why it throws an error.

Solution:
Write the formula again.

SELECT
    Product,
    Price * Quantity AS Revenue
FROM sales
WHERE Price * Quantity > 500;

Or later (in the next lesson), we’ll use CTE to make it neater.