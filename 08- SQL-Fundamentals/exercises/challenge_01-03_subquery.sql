USE data_science_journey;

#ch1-Show all products whose quantity is above the average quantity.

SELECT
    Product,
    Quantity
FROM sales
WHERE Quantity >
(
    SELECT AVG(Quantity)
    FROM sales
);

#ch2-Show all products whose price is equal to the highest price.

SELECT
    Product,
    Price
FROM sales
WHERE Price =
(
    SELECT MAX(Price)
    FROM sales
);

#ch3-Show all products whose price is below the average price.

SELECT
    Product,
    Price
FROM sales
WHERE Price <
(
    SELECT AVG(Price)
    FROM sales
);