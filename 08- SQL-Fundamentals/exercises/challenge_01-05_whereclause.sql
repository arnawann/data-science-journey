#Urutkan produk berdasarkan Category, lalu Quantity tertinggi.
USE data_science_journey;

#Challenge1 Show all products priced over200.

SELECT *
FROM sales
WHERE Price > 200;

#Challenge2 Show all productsin the Furniture categorywith a quantity greater than 2.

FROM sales
WHERE Category = 'Furniture'
AND Quantity > 2;

#Challenge 3 Show all productsin the Electronicsor Clothing categories.

SELECT *
FROM sales
WHERE Category = 'Electronics'
OR Category = 'Clothing';

#orbetter:

SELECT *
FROM sales
WHERE Category IN ('Electronics, Clothing');

#Challenge 4 Show all products priced between50 and500.

SELECT *
FROM sales
WHERE Price BETWEEN 50 AND 500;

#Challenge 5 Show all products whose names beginwith the letter P.

SELECT *
FROM sales
WHERE Product LIKE 'P%';

