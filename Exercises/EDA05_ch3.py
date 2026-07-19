#CH3-Top 3 Products by Quantity.
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

quantity = (
    df.groupby('Product')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print(quantity)