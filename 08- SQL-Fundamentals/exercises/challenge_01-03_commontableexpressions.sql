#CH-1 Display:
Create a CTE named
->RevenueTable
that contains:
-Product
-Revenue
Then display all Revenue values greater than 1000.

USE data_science_journey;

WITH RevenueTable AS
(
    SELECT
        Product,
        Price * Quantity AS Revenue
    FROM sales
)

SELECT
    Product,
    Revenue
FROM RevenueTable
WHERE Revenue > 1000;

#CH-2 Display:
Create a CTE
-> PriceTable
containing:
-Product
-Price
Then display all Prices greater than 500.

WITH PriceTable AS
(
    SELECT
        Product,
        Price
    FROM sales
)

SELECT
    Product,
    Price
FROM PriceTable
WHERE Price > 500;

#CH-3 Display:
Create a CTE
-> StockTable
containing:
-Product
-Quantity
Then display the highest Quantity.

#Option1
WITH StockTable AS
(
    SELECT
        Product,
        Quantity
    FROM sales
)
SELECT 
    Product,
    Quantity
FROM StockTable
ORDER BY Quantity DESC 
LIMIT 1;

#Option2(using subquery)
WITH StockTable AS
(
    SELECT
        Product,
        Quantity
    FROM sales
)

SELECT
    Product,
    Quantity
FROM StockTable
WHERE Quantity = 
(
    SELECT MAX(Quantity)
    FROM StockTable
);