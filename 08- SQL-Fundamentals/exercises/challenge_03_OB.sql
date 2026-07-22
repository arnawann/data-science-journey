#Urutkan produk berdasarkan Category, lalu Quantity tertinggi.
USE data_science_journey;

SELECT *
FROM sales
ORDER BY Category ASC, Quantity DESC;