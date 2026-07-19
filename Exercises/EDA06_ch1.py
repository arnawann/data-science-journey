#CH1=Create a chart : Average Price by Category
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

average_price = (
    df.groupby('Category')['Price']
    .mean()
)

plt.figure(figsize=(8,5))

plt.bar(
    average_price.index,
    average_price.values
)

plt.title("Average Price by Category")
plt.xlabel('Category')
plt.ylabel('Price')

plt.xticks(rotation=45)

plt.show()