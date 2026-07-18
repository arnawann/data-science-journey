import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/data/sales_data_dirty.csv")

print("===== DUPLICATE REPORT =====")

duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)

print("Rows Before:", len(df))

clean_df = df.drop_duplicates()

print("Rows After:", len(clean_df))

print("Rows Removed:", len(df) - len(clean_df))

print("\nRemaining Products:")

for product in clean_df["Product"].unique():
    print(product)