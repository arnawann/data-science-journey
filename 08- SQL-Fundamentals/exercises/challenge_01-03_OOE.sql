#CH-1 Display:
Product
Price
With the following criteria:
Price > 100
Sort from highest to lowest.

SELECT
    Product,
    Price
FROM sales
WHERE Price > 100
ORDER BY Price DESC;

#CH-2 Display:
Product
Revenue
Revenue = Price × Quantity
Provided that Revenue > 1000.
(Hint: Do not use the alias "Revenue" in the WHERE clause.)

SELECT
    Product,
    Price * Quantity AS Revenue
FROM sales
WHERE Price * Quantity > 1000;

#CH-3 Display:
Category
Total Quantity
Only categories where Total Quantity > 5.
(Hint: Use GROUP BY and HAVING.)

SELECT
    Category,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category
WHERE SUM(Quantity) > 5;