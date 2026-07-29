USE data_science_journey;

#78-date&timefunctions
Preparation
Since our sales table doesn't have a date column yet, let's add one first.

ALTER TABLE sales
ADD COLUMN OrderDate DATE;

UPDATE sales
SET OrderDate = '2026-07-01'
WHERE Produc = 'Laptop';

UPDATE sales
SET OrderDate = '2026-07-03'
WHERE Product = 'Phone';

UPDATE sales
SET OrderDate = '2026-07-05'
WHERE Product = 'Chair';

UPDATE sales
SET OrderDate = '2026-08-01'
WHERE Product = 'Mouse';

UPDATE sales
SET OrderDate = '2026-08-10'
WHERE Product = 'Table';

#78-YEAR()
#Display the year.

SELECT
    Product,
    OrderDate,
    YEAR(OrderDate) AS Order_Year
FROM sales;

#79-MONTH()

SELECT
    Product,
    OrderDate,
    MONTH(OrderDate) AS Order_Month
FROM sales;

#80-DAY()

SELECT
    Product,
    OrderDate,
    DAY(OrderDate) AS Order_Day
FROM sales;

#81-DATE_FORMAT()

SELECT
    Product,
    DATE_FORMAT(OrderDate, '%d-%m-%Y') AS Formatted_Date
FROM sales;

#82-DATEDIFF()
#Calculating the number of days between two dates.

SELECT
    Product,
    OrderDate,
    DATEDIFF(CURDATE(), OrderDate) AS Days_Ago
FROM sales;