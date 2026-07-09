import pandas as pd
students = {
    "Name": ["Ali", "Ahmad", "Sarah", "Fatimah", "Hasan"],
    "Age": [20,21,19,22,18],
    "Score": [85,90,88,95,80]
}
df = pd.DataFrame(students)
print(df)

print("==== Challenge 1 ====")
products = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Price": [15000, 500, 1200, 3500, 2500],
    "Stock": [5,20,12,8,6]
}
df = pd.DataFrame(products)

print("==== cetak semua ====")
print(df)

print("==== cetak hanya kolom product ====")
print(df["Product"])

print("==== cetak hanya kolom price ====")
print(df["Price"])

print("==== cetak kolom product dan price ====")
print(df[["Product", "Price"]])

print("==== Hitung ====")

print("+++ rata-rata price +++")
print("Average Price :", df["Price"].mean())

print("+++ harga tertinggi +++")
print("Highest Price :", df["Price"].max())

print("+++ harga terendah +++")
print("Lowest Price :", df["Price"].min())

print("+++ total semua harga +++")
print("Total Price :", df["Price"].sum())