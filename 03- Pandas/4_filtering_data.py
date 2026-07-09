print("=== Filtering Data===")
import pandas as pd 
products = {
    "Product": ["Laptop", "Tablet", "Smartphone", "Desktop", "Monitor"],
    "Price": [1215000, 500, 1200, 3500, 2500],
    "Stock": [5, 20, 12, 8, 6]
}

df = pd.DataFrame(products)
print(df)

print("=== Filtering Price > 2000===")
print(df[df["Price"] > 2000])

print("=== Filtering Stock > 10===")
print(df[df["Stock"] > 10])

print("=== Filtering Price < 3000===")
print(df[df["Price"] < 3000])

print("=== Filtering Price = 500===")
print(df[df["Price"] == 500])

print("=== Filter Tidak Sama Dengan 500 ===")
print(df[df["Price"] != 500])

print("=== Average Products Price > 2000 ===")
print(df[df["Price"] > 2000]["Price"].mean())