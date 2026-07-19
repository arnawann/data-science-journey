#Materi 3 — Average Price per Product
import pandas as pd

df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

price = df.groupby('Product')['Price'].mean()

print(price)