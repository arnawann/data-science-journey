#CHALLENGE 3 -  Combine ch1 & ch2 into a single replace()` ( Gabungkan ch1&ch2 menjadi satu replace() ).

import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

df["Category"] = df["Category"].replace({
    "electronics": "Electronics",
    "Clothng": "Clothing"
})

print(df["Category"].unique())