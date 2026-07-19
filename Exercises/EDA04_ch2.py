#Hitung Average Price per Product urutkan dari yang tertinggi.
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

price = (
    df.groupby('Product')['Price']
    .mean()
    .sort_values(ascending=False)
)

print(price)