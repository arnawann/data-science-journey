import pandas as pd #Highest Price per Category
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

print('===== CATEGORY REPORT =====')

df['Revenue'] = df['Price'] * df['Quantity']

revenue_by_category = df.groupby('Category')['Revenue'].sum()
average_price = df.groupby('Category')['Price'].mean()
average_quantity = df.groupby('Category')['Quantity'].mean()
product_count = df.groupby('Category')['Product'].count()
highest_price = df.groupby('Category')['Price'].max()
lowest_price = df.groupby('Category')['Price'].min()

print('\nRevenue by Category:')
print(revenue_by_category)
print('\nAverage Price by Category:')
print(average_price)
print('\nAverage Quantity by Category:')
print(average_quantity)
print('\nProduct Count by Category:')
print(product_count)
print('\nHighest Price by Category:')
print(highest_price)
print('\nLowest Price by Category:')
print(lowest_price)