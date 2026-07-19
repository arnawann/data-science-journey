import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

print("===== PRODUCT REPORT =====")

df['Revenue'] = df['Price'] * df['Quantity']

revenue = (
    df.groupby('Product')['Revenue']
    .sum()
)

quantity = ( 
    df.groupby('Product')['Quantity']
    .sum()
)

average_price = (
    df.groupby('Product')['Price']
    .mean()
)
top3 = (
    df.groupby('Product')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print('\nRevenue by Product:')
print(revenue)

print('\nQuantity Sold by Product:')
print(quantity)

print('\nAverage Price by Product:') 
print(average_price)

print('\nTop 3 Products by Revenue:') 
print(top3)