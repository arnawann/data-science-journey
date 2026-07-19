#Lesson 3 — Category with Highest Revenue
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

top_category = (
    df.groupby('Category')['Revenue']
    .sum()
    .idxmax()
)

print(top_category)