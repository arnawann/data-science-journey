import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

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