#Materi 5 - Using str.title() ( Menggunakan str.title() )

import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

df["Category"] = df["Category"].str.title()

print(df["Category"].unique())