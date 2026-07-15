import pandas as pd #ch3

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.dropna(axis=1)

print(clean_df.columns)