USE data_science_journey;

#74-row number
#OVER() means "Count for each row."

SELECT
    Product,
    Price

    ROW_NUMBER() OVER
    (
        ORDER BY Price DESC
    ) AS Row_Number

FROM sales;

#75-RANK()

SELECT
    Product,
    Price,

    RANK() OVER
    (
        ORDER BY Price DESC
    ) AS Price_Rank

FROM sales;

#76-DENSE_RANK()

SELECT
    Product,
    Price,

    DENSE_RANK() OVER
    (
        ORDER BY Price DESC
    ) AS Dense_Rank

FROM sales;

#77- PARTITION BY
#Now this is a Data Analysts favorite feature.

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