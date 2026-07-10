import pandas as pd
df = pd.read_csv("03- Pandas/data/sales_data.csv")
print(df)

print("=== Tambahkan Kolom Baru ===")
df["Revenue"] = df["Price"] * df["Quantity"]
print(df)

print("=== Total Revenue ===")
print(df["Revenue"].sum())

print("=== Produk Terlaris ===")
print(df.sort_values("Quantity", ascending=False))

print("=== Produk Omzet Terbesar ===")
print(df.nlargest(1, "Revenue"))

print("=== Revenue Tiap Kategori ===")
print(df.groupby("Category")["Revenue"].sum())

print("=== Harga rata-rata tiap kategori ===")
print(df.groupby("Category")["Price"].mean())

print("=== Jumlah produk tiap kategori ===")
print(df.groupby("Category")["Product"].count())

print("=== Challenge 1 - Cetak produk dengan harga di atas Rp2.000.000. ===")
print(df[df["Price"] > 2000000])

print("=== Challenge 2 - Cetak produk dengan Quantity lebih dari 8. ===")
print(df[df["Quantity"] >8])

print("=== Challenge 3 - Tampilkan hanya: Product dan Revenue ===")
print(df[["Product", "Revenue"]])

print("=== Challenge 4 - Cari produk dengan Revenue terbesar ===")
print(df.nlargest(1, "Revenue"))

print("=== Challenge 5 - Hitung: Revenue rata-rata, Revenue terbesar, dan Revenue terkecil ===")
print(df["Revenue"].mean())
print(df["Revenue"].max())
print(df["Revenue"].min())

print("=== Bonus Challenge ===")
print("=" * 40)
print("        SALES REPORT")
print("=" * 40)

print("Total Revenue : Rp", df["Revenue"].sum())

print("\nBest Selling Product :")
print(df.nlargest(1, "Quantity"))

print("\nHighest Revenue Product :")
print(df.nlargest(1, "Revenue"))

print("\nAverage Price :", df["Price"].mean())

print("\nRevenue by Category :") 
print(df.groupby("Category")["Revenue"].sum())