#miniprojectcasewhen
Add two new columns:

-Price_Label
Price >= 500 (Expensive)
Else (Affordable)
Sort by highest revenue.

-Revenue_Status
Revenue >=1000 (High Revenue)
Else (Low Revenue)
Sort by highest revenue.

USE data_science_journey;

SELECT
    Product,
    Category,
    Price,
    Quantity,
    Price * Quantity AS Revenue,

    CASE
        WHEN Price >= 500 THEN 'Expensive'
        ELSE 'Affordable'
    END AS Price_Label,

    CASE
        WHEN Price * Quantity >= 1000 THEN 'High Revenue'
        ELSE 'Low Revenue'
    END AS Revenue_Status

FROM sales
ORDER BY Revenue DESC;