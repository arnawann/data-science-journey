#Materi 1 — Cek Missing Value
import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print(df.isnull().sum())