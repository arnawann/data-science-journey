#Materi 3 — Average Quantity per Category
import pandas as pd
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

average_quantity = df.groupby('Category')['Quantity'].mean()

print(average_quantity)