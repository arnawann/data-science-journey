import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

print("===== DATA OVERVIEW =====")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())