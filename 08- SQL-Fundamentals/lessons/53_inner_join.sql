USE data_science_journey;

#Before Join
#Take a look at the contents of both tables first.

SELECT * FROM products;

#53- Inner Join

SELECT
    products.ProductName,
    orders.Quantity
FROM products
INNER JOIN orders
ON products.ProductID = orders.ProductID;

#Using Alias (Best Practice)
#In the workplace, almost everyone uses a alias, shorter and neater.

USE data_science_journey;

SELECT
    p.ProductName,
    o.Quantity
FROM products AS p
INNER JOIN orders AS o
ON p.ProductID = o.ProductID;

#addprice

SELECT
    p.ProductName,
    p.Price,
    o.Quantity
FROM products p
INNER JOIN orders o
ON p.ProductID = o.ProductID;

#addrevenue

SELECT
    p.ProductName,
    p.Price,
    o.Quantity,
    p.Price * o.Quantity AS Revenue
FROM products p
INNER JOIN orders o
ON p.ProductID = o.ProductID;
