#Materi 3 - Menghapus Duplikat (Removing Duplicates)

import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

clean_df = df.drop_duplicates()

print(clean_df)