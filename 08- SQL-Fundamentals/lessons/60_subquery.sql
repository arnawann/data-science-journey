USE data_science_journey;

#60-subquery

SELECT *
FROM sales
WHERE >
(
    SELECT AVG(Price)
    FROM sales
);

#61-Create a file

SELECT
    Product,
    Price
FROM sales
WHERE Price >
(
    SELECT AVG(Price)
    FROM sales
);

#62-The most expensive product.

SELECT
    Product,
    Price
FROM sales
WHERE Price =
(
    SELECT MAX(Price)
    FROM sales
);

#63-The cheapest product.

SELECT
    Product,
    Price
FROM sales
WHERE Price =
(
    SELECT MIN(Price)
    FROM sales
);