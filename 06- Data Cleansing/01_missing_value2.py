import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print(df.isnull().sum())

#Materi 2 — Menghitung jumlah missing value