#Lesson 1 — Product with Highest Revenue
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

top_product = (
    df.groupby('Product')['Revenue']
    .sum()
    .idxmax()
)

print(top_product)