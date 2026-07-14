import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print("===== DATA QUALITY REPORT =====")

print("Dataset has missing value:", df.isnull().values.any())

print("\nMissing Value by Column")

print(df.isnull().sum())

print("\nTotal Missing Value:", df.isnull().sum().sum())

#Missing Value Mini Project