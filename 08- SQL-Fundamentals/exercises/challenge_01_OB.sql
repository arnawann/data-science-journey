#Tampilkan 3 produk dengan Quantity terbesar.
USE data_science_journey;

SELECT *
FROM sales
ORDER BY Quantity DESC
LIMIT 3;