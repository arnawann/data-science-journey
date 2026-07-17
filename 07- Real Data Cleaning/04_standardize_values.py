#Materi 1 — Melihat Nilai Unik (Seeing Unique Value)

import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print(df["Category"].unique())