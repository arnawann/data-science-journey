#Materi 2 — Mengganti banyak nilai sekaligus

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Category"] = df["Category"].replace({
    "Electronics":"Electronic Devices",
    "Furniture":"Home Furniture"
})

print(df)