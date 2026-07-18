import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

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
print(df['Revenue'].mean)

print('\nHighest Revenue:')
print(df['Revenue'].max)

print('\nLowest Revenue:')
print(df['Revenue'].min)

print('\n Standard Deviation (Price):')
print(df["Price"].std())

print('\nFull Statistics:')
print(df.describe())