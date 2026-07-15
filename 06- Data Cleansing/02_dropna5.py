import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df.dropna(inplace=True)

print(df)

#Materi 5 - Menghapus langsung pada DataFrame asli
# kalau ingin langsung mengubah DataFrame asli
# inplace=True