import pandas as pd #ch1

df = pd.read_csv("03- Pandas/data/sales_data.csv")

print(("Rows before :"), len(df))

clean_df = df.dropna()

print(("Rows after :"), len(clean_df))
