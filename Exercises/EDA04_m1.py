#Materi 1 — Total Revenue per Product
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

revenue = df.groupby('Product')['Revenue'].sum()

print(revenue)