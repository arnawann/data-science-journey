#Materi 3 — Mengisi dengan rata-rata (Mean)
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

mean_price = df["Price"].mean()

df["Price"] = df["Price"].fillna(mean_price)

print(df)