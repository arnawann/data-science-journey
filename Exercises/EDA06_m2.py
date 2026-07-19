#Lesson 2 — Quantity Sold by Category
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

quantity = (
    df.groupby('Category')['Quantity']
    .sum()
)

plt.bar(quantity.index, quantity.values)

plt.title('Quantity Sold by Category')

plt.xlabel('Category')

plt.ylabel('Quantity')

plt.show()