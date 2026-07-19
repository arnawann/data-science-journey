#CH1-Show Products with the highest sales volume
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

quantity = (
    df.groupby('Product')['Quantity']
    .sum()
    .idxmax()
)

print(quantity)