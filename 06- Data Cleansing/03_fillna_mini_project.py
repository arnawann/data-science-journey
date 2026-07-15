print("===== DATA FILLING REPORT =====")

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print("Missing Value Before:", df.isnull().sum().sum())

filled_df = df.fillna(0)

print("Missing Value After:", filled_df.isnull().sum().sum())

print("\nFilled Dataset:")

print(filled_df)