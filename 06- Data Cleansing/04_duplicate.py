#Materi 1 — Mengecek data duplikat
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print(df.duplicated())