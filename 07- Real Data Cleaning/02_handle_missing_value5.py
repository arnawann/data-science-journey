#Materi 5 — Drop Missing Value

import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

clean_df = df.dropna()

print(clean_df)