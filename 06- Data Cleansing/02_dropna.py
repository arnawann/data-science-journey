import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print("Before:", len(df))

clean_df = df.dropna()

print("After:", len(clean_df))

#Materi 1 — Menghapus semua baris yang memiliki missing value