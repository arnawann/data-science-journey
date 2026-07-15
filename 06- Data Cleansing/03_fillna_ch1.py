import pandas as pd #ch1

df = pd.read_csv("03- Pandas/data/sales_data.csv")

filled_df = df.fillna(0)

print(filled_df)