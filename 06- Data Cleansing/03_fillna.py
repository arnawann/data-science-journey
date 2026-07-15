#Materi 1 — Mengisi semua missing value dengan angka tertentu
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

filled_df = df.fillna(0)

print(filled_df)