#Materi 1 — Mengecek Data Duplikat (Checking for Duplicate Data)

import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print(df.duplicated())

print("\nTotal Duplicates:", df.duplicated().sum())
      