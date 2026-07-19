#miniproject-Create 3 consecutive charts: 1)Revenue by Category 2) Quantity by Category 3) Top 5 Products by Revenue
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

print('===== SALES DASHBOARD =====')
plt.figure(figsize=(14,10))

#---
# Revenue by Category
#---

plt.subplot(2,2,1)

revenue = (
    df.groupby('Category')['Revenue']
    .sum()
)

plt.bar(
    revenue.index,
    revenue.values
)

plt.title('Revenue by Category')

#---
# Quantity by Category
#---

plt.subplot(2,2,2)

quantity = (
    df.groupby('Category')['Quantity']
    .sum()
)

plt.bar(
    quantity.index,
    quantity.values
)

plt.title('Quantity by Category')

#---
#Top 5 Products
#---

plt.subplot(2,2,3)

top5 = (
    df.groupby('Revenue')['Product']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.bar(
    top5.index, 
    top5.values
)

plt.title("Top 5 Products by Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()