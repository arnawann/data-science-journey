#Materi 3 — Menghapus data duplikat

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.drop_duplicates()

print(clean_df)