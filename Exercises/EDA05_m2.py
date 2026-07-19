#Lesson 2 — Product with Lowest Revenue
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

bottom_product = (
    df.groupby('Product')['Revenue']
    .sum()
    .idxmin()
)

print(bottom_product)