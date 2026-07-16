import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print("===== DATA INSPECTION =====\n")

print(df)

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Categories:")
print(df["Category"].unique())