USE data_science_journey;

#Lesson 39 — HAVING

SELECT
    Category,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category
HAVING SUM(Quantity) > 10;

#Lesson 40 — HAVING + AVG

SELECT
    Category,
    AVG(Price) AS Average_Price
FROM sales
GROUP BY Category
HAVING AVG(Price) > 100;

#Lesson 41 - HAVING + COUNT

SELECT
    Category,
    COUNT(*) AS Total_Product
FROM sales
GROUP BY Category
HAVING COUNT(*) >= 3;

#Lesson 42 - HAVING + Multiple Aggregation

SELECT
    Category,
    COUNT(*) AS Total_Product,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category
HAVING SUM(Quantity) > 8;

#Lesson 41 - HAVING + ORDER BY

SELECT
    Category,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category
HAVING SUM(Quantity) > 5
ORDER BY Total_Quantity DESC;
