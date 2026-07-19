#Materi 2 — Average Price per Category
import pandas as pd
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

average_price = df.groupby("Category")['Price'].mean()

print(average_price)