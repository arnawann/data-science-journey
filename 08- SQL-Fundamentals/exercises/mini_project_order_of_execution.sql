#Mini Project
Create a report that displays:
Product
Category
Price
Quantity
Revenue
With the following conditions:
Revenue > 500
Sorted by highest Revenue.
Display only the top 5 entries.
USE data_science_journey;

-- ======================
-- ORDER OF EXECUTION REPORT
-- ======================

SELECT
    Product,
    Category,
    Price,
    Quantity,
    Price * Quantity AS Revenue
FROM sales
WHERE Price * Quantity > 500
ORDER BY Revenue DESC
LIMIT 5;