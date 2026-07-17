import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print("===== VALUE STANDARDIZATION REPORT =====")

print("\nBefore:")

print(df["Category"].unique())

df["Category"] = df["Category"].replace({
    "electronics": "Electronics",
    "Clothng": "Clothing"
})

print("\nAfter:")

print(df["Category"].unique())