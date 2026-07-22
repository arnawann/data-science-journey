USE data_science_journey;

#larger than

SELECT *
FROM sales
WHERE Price > 100;

#smaller

SELECT *
FROM sales
WHERE Price < 100;

#Thesameas

SELECT *
FROM sales
WHERE Category = 'Furniture';

#notthesame

SELECT *
FROM sales
WHERE Category <> 'Electronics';

#notthesame

SELECT *
FROM sales
WHERE Category != 'Electronics';