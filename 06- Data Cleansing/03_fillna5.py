#Materi 5 — Mengisi dengan Teks

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Category"] = df["Category"].fillna("Unknown")

print(df)