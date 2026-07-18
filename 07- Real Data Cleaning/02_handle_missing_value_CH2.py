import pandas as pd #ch2

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

median_quantity = df["Quantity"].median()

df["Quantity"] = df["Quantity"].fillna(median_quantity)

print(df)

