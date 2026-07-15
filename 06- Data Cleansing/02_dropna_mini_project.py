print("===== DATA CLEANING REPORT =====") #miniproject

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print("Rows Before:", len(df))

clean_df = df.dropna()

print("Rows After:", len(clean_df))

rows_removed = len(df) - len(clean_df)

print("Rows Removed:", rows_removed)

print("\nRemaining Columns:")

for col in clean_df.columns:
    print(col)
