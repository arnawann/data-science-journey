import pandas as pd #ch3-Hapus duplikat berdasarkan kolom Category.

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.drop_duplicates(subset=["Category"])

print(clean_df)