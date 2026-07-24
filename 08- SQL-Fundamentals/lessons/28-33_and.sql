USE data_science_journey;
#LESSON28-33

#28-AND

SELECT *
FROM sales
WHERE Category = 'Electronics'
AND Price > 100;

#29-OR

SELECT *
FROM sales
WHERE Category = 'Furniture'
OR Category = 'Clothing';

#30-BETWEEN

SELECT *
FROM sales
WHERE Price BETWEEN 50 AND 500;

#atau

WHERE Price >= 50
AND Price <=5oo;

#31-IN

SELECT *
FROM sales
WHERE Category IN:
('Furniture', 'Clothing', 'Electronics');

#32-LIKE #Cari produk yang dimulai huruf P.

SELECT *
FROM sales
WHERE Product LIKE 'P%';

#Cari produk yang diakhiri huruf r

SELECT *
FROM sales
WHERE Product LIKE '%r';

#Cari yang mengandung huruf a

SELECT *
FROM sales
WHERE Product LIKE '%a%';

#33-NOT

SELECT *
FROM sales
WHERE NOT Category = 'Electronic';