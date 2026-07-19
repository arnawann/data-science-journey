#Show Top 3 Products berdasarkan Revenue.
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

top3 = (
    df.groupby('Product')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print(top3)