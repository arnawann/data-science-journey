#Materi 5 — Top Product
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df["Revenue"] = df["Price"] * df["Quantity"]

revenue = (
    df.groupby('Product')['Revenue']
    .sum()
    .sort_values(ascending=False)
)

print(revenue.head(1))