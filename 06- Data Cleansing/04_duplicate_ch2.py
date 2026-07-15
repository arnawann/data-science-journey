import pandas as pd #ch2-Hapus semua data duplikat.

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.drop_duplicates()

print(clean_df)