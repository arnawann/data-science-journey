#CH2=Create a chart : Quantity Sold by Product
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

quantity = (
    df.groupby('Product')['Quantity']
    .sum()
)

plt.figure(figsize=(8,5))

plt.bar(
    quantity.index, 
    quantity.values
)

plt.title("Quantity Sold by Product")

plt.xlabel('Product')

plt.ylabel('Quantity')

plt.xticks(rotation=45)

plt.show()