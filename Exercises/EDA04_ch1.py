#Hitung Total Quantity Sold per Product lalu urutkan dari yang terbesar.
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

quantity = (
    df.groupby('Product')['Quantity']
    .sum()
    .sort_values(ascending=False)
)

print(quantity)