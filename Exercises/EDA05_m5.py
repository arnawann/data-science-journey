#Lesson 5 — Top 5 Products
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

top5 = (
    df.groupby('Product')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top5)