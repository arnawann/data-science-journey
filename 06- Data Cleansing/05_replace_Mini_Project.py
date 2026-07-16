import pandas as pd #miniproject

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print("===== DATA REPLACEMENT REPORT =====")

print("Before Replacement")
print(df["Category"].unique())

df["Category"]=df["Category"].replace({
    "Electronics":"Electronic Devices",
    "Furniture":"Home Furniture",
    "Clothing":"Fashion"
})

print("After Replacement")
print(df["Category"].unique())

