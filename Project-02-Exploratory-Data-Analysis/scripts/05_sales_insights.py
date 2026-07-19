import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

print('===== SALES INSIGHTS =====')

highest_revenue_product = (
    df.groupby('Product')['Revenue']
    .sum()
    .idxmax()
)

lowest_revenue_product = (
    df.groupby('Product')['Revenue']
    .sum()
    .idxmin()
)

highest_revenue_category = (
    df.groupby('Category')['Revenue']
    .sum()
    .idxmax()
)

average_revenue_product = (
    df.groupby('Product')['Revenue']
    .mean()
)

top5 = (
    df.groupby('Revenue')['Product']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print('\nHighest Revenue Product:')
print(highest_revenue_product)

print('\nLowest Revenue Product:')
print(lowest_revenue_product)

print('\nHighest Revenue Category:')
print(highest_revenue_category)

print('\nAverage Revenue Product:')
print(average_revenue_product)

print('\nTop 5 Products by Revenue:')
print(top5)