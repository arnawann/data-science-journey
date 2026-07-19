#CH3=Create a chart : Top 5 Products by Revenue
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

top5 = (
    df.groupby('Product')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(8,5))

plt.bar(
    top5.index, 
    top5.values
)

plt.title("Top 5 Products by Revenue")

plt.xlabel('Category')

plt.ylabel('Price')

plt.xticks(rotation=45)

plt.show()