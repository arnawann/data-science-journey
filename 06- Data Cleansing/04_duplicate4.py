#Materi 4 — Menghapus duplikat berdasarkan kolom tertentu

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.drop_duplicates(subset=["Product"])

print(clean_df)