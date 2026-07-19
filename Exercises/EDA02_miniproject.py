import pandas as pd

df = pd.read_csv("Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv")

df['Revenue'] = df['Price'] * df['Quantity']

print("\nTotal Products:", df['Product'].nunique())

print("\nAverage Price:", df['Price'].mean())

print("\nMedian Price:", df['Price'].median())

print("\nHighest Price:", df['Price'].max())

print("\nLowest Price:", df['Price'].min())

print("\nTotal Quantity Sold:", df['Quantity'].sum())

print("\nAverage Revenue:", df['Revenue'].mean())

print("\nTotal Revenue:", df['Revenue'].sum())

print("\nHighest Revenue:", df['Revenue'].max())

print("\nLowest Revenue:", df['Revenue'].min())

print("\nStandard Deviation (Price):", df['Price'].std())



