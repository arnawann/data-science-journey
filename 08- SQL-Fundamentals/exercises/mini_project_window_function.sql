#miniprojectwindowfunction
🚀 Mini Project

Create a report

Displaying

Product
Category
Price
Revenue

Add

Overall_Rank

using

ROW_NUMBER()

based on the highest Revenue.

Also add

Category_Rank

using

PARTITION BY Category

based on the highest Revenue.

Sort by highest Revenue.


-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

SELECT
    Product,
    Category,
    Price,
    Price * Quantity AS Revenue

    ROW_NUMBER() OVER
    (
        ORDER BY Price * Quantity DESC
    ) AS Overall_Rank,

    ROW_NUMBER() OVER
    (
        PARTITION BY Category
        ORDER BY Price * Quantity DESC
    ) AS Category_Rank

FROM sales
ORDER BY Revenue DESC;