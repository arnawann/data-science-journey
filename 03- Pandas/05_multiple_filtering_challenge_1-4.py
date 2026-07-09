import pandas as pd
products = {
    "Product": ["Laptop", "Tablet", "Smartphone", "Desktop", "Monitor"],
    "Price": [1215000, 500, 1200, 3500, 2500],  
    "Stock": [2,20,12,8,6]
}
df = pd.DataFrame(products)
print(df)

print("==== Challenge 1 ====")
print(df[(df["Price"] > 2000) & (df["Stock"] > 5)])

print("==== Challenge 2 ====")
print(df[(df["Price"] < 2000) | (df["Stock"] < 10)])

print("==== Challenge 3 ====")
print(df[(df["Price"] >= 2500) & (df["Stock"] <= 8)])

print("==== Challenge 4 ====")
print(df[(df["Price"] < 3000) & (df["Stock"] > 10)])

print("==== Challenge Bonus ====")
print("Average Price:", df[(df["Price"] > 2000) & (df["Stock"] > 5)]["Price"].mean())