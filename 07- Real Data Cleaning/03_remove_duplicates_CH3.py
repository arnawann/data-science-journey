import pandas as pd #CH3-Hapus semua data duplikat dan tampilkan jumlah baris sebelum dan sesudah. (Remove all duplicate data and display the number of rows before and after.)

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print("Rows Before:", len(df))

clean_df = df.drop_duplicates()

print("Rows After:", len(clean_df))

print("Rows Removed:", len(df) - len(clean_df))