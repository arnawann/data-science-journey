USE data_science_journey;

#73-common table expressions
#Revenue is now calculated only once.

WITH RevenueTable AS
(
    SELECT
        Product,
        Category,
        Price,
        Quantity,
        Price * Quantity AS Revenue
    FROM sales
)

SELECT *
FROM RevenueTable
WHERE Revenue > 500
ORDER BY Revenue DESC;

#74 CTE Basic

WITH RevenueTable AS
(
    SELECT
        Product,
        Category,
        Price,
        Quantity,
        Price * Quantity AS Revenue
    FROM sales
)

SELECT
    Product,
    Revenue
FROM RevenueTable;

#75-Filter Revenue

WITH RevenueTable AS
(
    SELECT
        Product,
        Category,
        Price,
        Quantity,
        Price * Quantity AS Revenue
    FROM sales
)

SELECT
    Product,
    Revenue
FROM RevenueTable
WHERE Revenue > 500;

Take note.
Now

-> WHERE Revenue

is acceptable.

Why?

Because Revenue has already been defined in the CTE.

#76-Sorting

WITH Revenue AS
(
    SELECT
        Product,
        Category,
        Price,
        Quantity,
        Price * Quantity AS Revenue
    FROM sales
)

SELECT *
FROM RevenueTable
ORDER BY Revenue DESC;