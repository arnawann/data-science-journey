#Buat laporan SQL yang menampilkan:
#Semua produk diurutkan berdasarkan Price tertinggi.
#Top 5 produk termahal.
#Top 3 Quantity terbesar.
#Produk diurutkan berdasarkan Category lalu Price.

USE data_science_journey;

-- ======================
-- All Products by Highest Price
-- ======================

SELECT *
FROM sales
ORDER BY Price DESC;

-- ======================
-- All Products by Highest Price
-- ======================

SELECT *
FROM sales
ORDER BY Price DESC
LIMIT 5;

-- ======================
-- Top 3 Highest Quantity
-- ======================

SELECT *
FROM sales
ORDER BY Quantity DESC
LIMIT 3;

-- ======================
-- Products by Category then Price
-- ======================

SELECT *
FROM sales
ORDER BY Category ASC, Price DESC;