import pandas as pd #ch1-Hitung jumlah data duplikat.

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print(df.duplicated().sum())