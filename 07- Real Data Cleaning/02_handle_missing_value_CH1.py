#ch1 isi missing value pada kolom Price menggunakan mean.
import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

mean_price = df["Price"].mean()

df["Price"] = df["Price"].fillna(mean_price)

print(df)