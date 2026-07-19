import pandas as pd #Total Quantity per Category
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

total_quantity = df.groupby('Category')['Quantity'].sum()

print("Total Quantity per Category:")
print(total_quantity)