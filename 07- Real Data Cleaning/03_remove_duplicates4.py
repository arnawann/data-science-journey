#Materi 4 - Menghapus Berdasarkan Kolom Tertentu ( Deleting Based on a Specific Column)
import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

clean_df = df.drop_duplicates(subset=["Product"])

print(clean_df)