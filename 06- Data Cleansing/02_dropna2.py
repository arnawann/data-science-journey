import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.dropna(subset=["Price"])

print(clean_df)

#Materi 2 - Menghapus baris hanya jika kolom tertentu kosong
# dropna(subset=[])
