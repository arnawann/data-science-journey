#Materi 2 — Mengisi hanya kolom tertentu
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Price"] = df["Price"].fillna(0)

print(df)
