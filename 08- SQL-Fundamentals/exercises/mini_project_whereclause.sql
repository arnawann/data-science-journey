#miniprojectwhereclause

-- ===========
-- SQL REPORT
-- ===========

USE data_science_journey;

-- ===========
-- All electronics products priced above 100.
-- ===========

SELECT *
FROM sales
WHERE Category='Electronics'
AND Price>100;

-- ===========
-- All furniture with a quantity of 3 or more.
-- ===========

SELECT *
FROM sales
WHERE Category='Furniture'
AND Quantity >= 3;

-- ===========
-- All products priced between 100 and 1,000.
-- ===========

SELECT *
FROM sales
WHERE Price BETWEEN 100 AND 1000;

-- ===========
-- All products whose names contain the letter "o."
-- ===========

SELECT *
FROM sales
WHERE Product LIKE '%o%';

-- ===========
-- All products except Clothing.
-- ===========

SELECT *
FROM sales
WHERE Category <> 'Clothing';

#oralsocan

SELECT *
FROM sales
WHERE NOT Category = 'Clothing';