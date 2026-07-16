#ch1 isi missing value pada kolom Price menggunakan mean.
import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

mean_price = df["Price"].mean()

df["Price"] = df["Price"].fillna(mean_price)

print(df)