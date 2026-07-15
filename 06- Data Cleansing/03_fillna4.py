#Materi 4 — Mengisi dengan Median
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

median_price = df["Price"].median()

df["Price"] = df["Price"].fillna(median_price)

print(df)