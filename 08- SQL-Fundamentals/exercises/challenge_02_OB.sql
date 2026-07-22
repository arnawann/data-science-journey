#Tampilkan 5 produk termurah.
USE data_science_journey;

SELECT *
FROM sales
ORDER BY Price
LIMIT 5;