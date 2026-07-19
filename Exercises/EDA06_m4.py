#Lesson 4 — Rotate Labels
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

revenue = (
    df.groupby('Product')['Revenue']
    .sum()
)

plt.bar(revenue.index, revenue.values)

plt.title('Revenue by Product')

plt.xlabel('Product')

plt.ylabel('Revenue')

plt.xticks(rotation=45)

plt.show()