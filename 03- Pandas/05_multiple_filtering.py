import pandas as pd 
products = {
    "Product": ["Laptop", "Tablet", "Smartphone", "Desktop", "Monitor"],
    "Price": [1215000, 500, 1200, 3500, 2500],  
    "Stock": [2,20,12,8,6]
}
df = pd.DataFrame(products)
print(df)

print("=== AND Filter ===")
print(df[(df["Price"] > 2000) & (df["Stock"] > 5)])

print("=== OR Filter ===")
print(df[(df["Price"] < 2000) | (df["Stock"] < 10)])

print("=== AND + OR Filter ===")
print(df[((df["Price"] >2000) & (df["Stock"] > 5)) | (df["Product"] != "Desktop")])
