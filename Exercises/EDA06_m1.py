#Lesson 1 — Revenue by Category (Bar Chart)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df["Revenue"] = df["Price"] * df["Quantity"]

revenue = (
    df.groupby('Category')['Revenue']
    .sum()
)

plt.bar(revenue.index, revenue.values)

plt.title('Revenue by Category')

plt.xlabel('Category')

plt.ylabel('Revenue')

plt.show()