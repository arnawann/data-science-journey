#CH2-Category with the highest average price.
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

category = (
    df.groupby('Category')['Price']
    .mean()
    .idxmax()
)

print(category)