import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/data/sales_data_dirty.csv")

print("===== VALUE STANDARDIZATION REPORT =====")

print("\nBefore:")

print(df["Category"].unique())

df["Category"] = df["Category"].replace({
    "electronics": "Electronics",
    "Clothng": "Clothing"
})

df["Category"] = df["Category"].str.title()

print("\nAfter:")

print(df["Category"].unique())