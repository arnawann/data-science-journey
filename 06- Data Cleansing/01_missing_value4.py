import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print(df.isnull().sum().sum())

#Materi 4 — Total missing value seluruh dataset