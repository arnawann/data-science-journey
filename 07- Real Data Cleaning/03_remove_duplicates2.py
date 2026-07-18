#Materi 2 — Melihat Baris yang Duplikat (Viewing Duplicate Rows)

import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

duplicates = df[df.duplicated()]

print(duplicates)