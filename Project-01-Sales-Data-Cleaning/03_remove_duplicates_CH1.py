import pandas as pd #CH1-Hitung Jumlah Data Duplikat (Count the Number of Duplicate Data Points)

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

print(df.duplicated())

print("Total Duplicates:", df.duplicated().sum())