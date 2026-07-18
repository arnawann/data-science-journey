#Mini Project

import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_dirty_data.csv")

# Missing Values
df["Price"] = df["Price"].fillna
df["Quantity"] = df["Quantity"].fillna

# Duplicates
df.duplicates= df.dropna()

# Standardize
print(df["Category"], unique())

# Export
df.to_csv("07- Real Data Cleaning/cleaned_sales_data.csv")

print()