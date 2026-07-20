# ======================================
# PROJECT 02 - EXPLORATORY DATA ANALYSIS
# ======================================

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

print("===== DATA OVERVIEW =====")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())

print('===== DESCRIPTIVE STATISTICS =====')

# Revenue
df['Revenue'] = df['Revenue'] * df['Quantity']

print('\nAverage Price:')
print(df['Price'].mean())

print('\nMedian Price:')
print(df['Price'].median())

print('\nHighest Price:')
print(df['Price'].max())

print('\nLowest Price:')
print(df['Price'].min())

print('\nAverage Quantity:')
print(df['Quantity'].mean())

print('\nAverage Revenue:')
print(df['Revenue'].mean())

print('\nHighest Revenue:')
print(df['Revenue'].max())

print('\nLowest Revenue:')
print(df['Revenue'].min())

print('\n Standard Deviation (Price):')
print(df["Price"].std())

print('\nFull Statistics:')
print(df.describe())

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

print('===== SALES DASHBOARD =====')
plt.figure(figsize=(10,8))

#---
# Revenue by Category
#---

plt.subplot(3,1,1)

revenue = (
    df.groupby('Category')['Revenue']
    .sum()
)

plt.bar(
    revenue.index,
    revenue.values,
    color='steelblue'
)

plt.grid(axis='y', alpha=0.3)

plt.title(
    'Revenue by Category',
    weight="bold"
)
plt.xlabel('Category')
plt.ylabel('Revenue')

#---
# Quantity by Category
#---

plt.subplot(3,1,2)

quantity = (
    df.groupby('Category')['Quantity']
    .sum()
)

plt.bar(
    quantity.index,
    quantity.values,
    color='orange'
)

plt.grid(axis='y', alpha=0.3)

plt.title(
    'Quantity by Category',
    weight="bold"
)
plt.xlabel('Category')
plt.ylabel('Quantity')

#---
#Top 5 Products
#---

plt.subplot(3,1,3)

top5 = (
    df.groupby('Product')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.bar(
    top5.index, 
    top5.values,
    color=['green', 'orange', 'gold', 'green', 'blue']
)

plt.grid(axis='y', alpha=0.3)

plt.title(
    "Top 5 Products by Revenue",
    weight="bold"
)
plt.xlabel('Product')
plt.ylabel('Revenue')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()