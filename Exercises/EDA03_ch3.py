import pandas as pd #Lowest Price per Category
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

lowest_price = df.groupby('Category')['Price'].min()

print("Lowest Price per Category:")
print(lowest_price)