USE data_science_journey;

#64-subquery with in
For example, let say we want to display all products in a category where the price is above 500.

SELECT
    Product,
    Category,
    Price
FROM sales
WHERE Category IN
(
    SELECT Category
    FROM sales
    WHERE Price > 500
);

For example, if the subquery returns

Electronics
Furniture

then the main query becomes:

SELECT
    Product,
    Category,
    Price
FROM sales
WHERE Category IN
(
    'Electronics',
    'Furniture'
);

#65 Subquery NOT IN
e.g.: Display categories that do not include high-priced products.

SELECT
    Product,
    Category
FROM sales
WHERE Category NOT IN
(
    SELECT Category
    FROM sales
    WHERE Price > 500
);

#66 A subquery can also return a list of products.

SELECT
    Product,
    Price
FROM sales
WHERE Product IN
(
    SELECT Product
    FROM sales
    WHERE Quantity >= 3
);