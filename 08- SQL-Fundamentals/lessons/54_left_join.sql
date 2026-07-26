USE data_science_journey;

#54-LEFT JOIN (RIGHT JOIN IS VICE VERSA)

SELECT
    p.ProductName,
    o.Quantity
FROM products p
LEFT JOIN orders o
ON p.ProductID = o.ProductID;

#Display 0 instead of NULL
#The dashboard is easier to read.

SELECT
    p.ProductName,
    IFNULL(o.Quantity,0) AS Quantity
FROM products p
LEFT JOIN orders o
ON p.ProductID = o.ProductID;