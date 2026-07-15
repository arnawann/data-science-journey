#Materi 5 — Menghapus langsung pada DataFrame asli
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df.drop_duplicates(inplace=True)

print(df)