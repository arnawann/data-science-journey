#miniprojectcommontableexpressions
🚀 Mini Project
Create
-> WITH SalesReport AS (...)
Columns:
-Product
-Category
-Price
-Quantity
-Revenue
Then
Display:
-Product
-Revenue
Where: Revenue > 500
Sort by highest Revenue.

WITH SalesReport AS
(
    SELECT
        Product,
        Category,
        Price,
        Quantity,
        Price * Quantity AS Revenue
    FROM sales
)
SELECT Product, Revenue
FROM SalesReport
WHERE Revenue > 500
ORDER BY REVENUE DESC;