#Materi 1 — Melihat Nilai Unik (Seeing Unique Value)

import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

print(df["Category"].unique())