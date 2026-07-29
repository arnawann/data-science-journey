#ch1- Display
Product
Price
Sort
ROW_NUMBER()
by highest Price.

SELECT
    Product,
    Price,
    ROW_NUMBER() OVER
    (
        ORDER BY Price DESC
    ) AS Row_Number
FROM sales;

#ch2- Display
Product
Price
Sort
RANK()
by highest Price.

SELECT
    Product,
    Price,
    RANK() OVER
    (
        ORDER BY Price DESC
    ) AS Price_Rank
FROM sales;

#ch3- Display
Product
Category
Price
Assign a ranking within each category.

Use

PARTITION BY

SELECT
    Product,
    Category,
    Price,
    ROW_NUMBER() OVER
    (
        PARTITION BY Category
        ORDER BY Price DESC
    ) AS Category_Rank
FROM sales;

