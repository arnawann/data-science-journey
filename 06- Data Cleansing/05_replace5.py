#Materi 5 - Mengganti langsung DataFrame asli

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df.replace(
    "Electronics",
    "Electronic Devices",
    inplace=True
)

print(df)