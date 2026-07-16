#Materi 4 — Isi Semua Missing Value Sekaligus

import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

df = df.fillna(0)

print(df)