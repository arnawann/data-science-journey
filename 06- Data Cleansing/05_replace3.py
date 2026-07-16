#Materi 3 — Mengganti angka tertentu

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Price"] = df["Price"].replace(
    500,
    550
)

print(df)