#Materi 2 — Menghitung jumlah data duplikat
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print(df.duplicated().sum())