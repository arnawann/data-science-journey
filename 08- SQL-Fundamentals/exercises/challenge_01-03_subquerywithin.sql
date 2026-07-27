#CH-1 Display all products in the same category as the products priced above 300.
SELECT
    Product,
    Category,
    Price
FROM sales
WHERE Category IN
(
    SELECT Category
    FROM sales
    WHERE Price > 300
);

#CH-2 Show all products that are not from categories with prices above 300.

SELECT
    Product,
    Category,
    Price
FROM sales
WHERE Category NOT IN
(
    SELECT Category
    FROM sales
    WHERE Price > 300
);

#CH3-Display all products whose names include products with a minimum quantity of 3.

SELECT
    Product,
    Quantity
FROM sales
WHERE Product IN
(
    SELECT Product
    FROM sales
    WHERE Quantity >= 3
);
