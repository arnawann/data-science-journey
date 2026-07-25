USE data_science_journey;

#47- Create a new table, products
CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);

#48- insert_products

INSERT INTO products VALUES
(1,'Laptop','Electronics',1200),
(2,'Mouse','Electronics',20),
(3,'Chair','Furniture',150),
(4,'Phone','Electronics',900),
(5,'Table','Furniture',200);

#49- Now create the second table, orders
CREATE TABLE orders (
    OrderID INT PRIMARY KEY,
    ProductID INT,
    Quantity INT
);

#50- Now enter the data, insert orders
INSERT INTO orders VALUES
(101,1,2),
(102,2,5),
(103,4,1),
(104,5,3);

#51 - SHOW TABLES;

#52 - View the contents
SELECT * FROM products;

#and

SELECT * FROM orders;