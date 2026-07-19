#Lesson 4 — Average Revenue per Product
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

average_revenue = (
    df.groupby('Product')['Revenue']
    .mean()
)

print(average_revenue)