USE data_science_journey;

#Lesson 34 — GROUP BY
#Pandas:df.groupby("Category")

SELECT Category
FROM sales
GROUP BY Category;

#Lesson 35 — SUM + GROUP BY
#Pandas:df.groupby("Category")["Quantity"].sum()

SELECT
    Category,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Category;

#Lesson 36 — AVG + GROUP BY
#Pandas:df.groupby("Category")["Price"].mean()

SELECT
    Category,
    AVG(Price) AS Average_Price
FROM sales
GROUP BY Category;

#Lesson 37 — COUNT + GROUP BY
#Pandas:df.groupby("Category")["Product"].count()

SELECT
    Category,
    COUNT(*) AS Total_Product
FROM sales
GROUP BY Category;

#Lesson 38 — Multiple Aggregation

SELECT
    Category,
    COUNT(*) AS Total_Product,
    SUM(Quantity) AS Total_Quantity,
    AVG(Price) AS Average_Price,
    MAX(Price) AS Highest_Price,
    MIN(Price) AS Lowest_Price
FROM sales
GROUP BY Category;
