import pandas as pd #ch3

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Category"] = df["Category"].replace({
    "Electronics":"Electronic Devices",
    "Furniture":"Home Furniture",
    "Clothing":"Fashion"
})

print(df)