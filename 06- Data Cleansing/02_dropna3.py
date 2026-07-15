import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.dropna(axis=1)

print(clean_df.columns)

#Materi 3 - Menghapus kolom yang memiliki missing value
# dropna(axis=1)
