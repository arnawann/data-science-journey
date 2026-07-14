import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print(df.isnull().any())

#Materi 3 — Mengetahui apakah dataset memiliki missing value