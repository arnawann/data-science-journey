import pandas as pd #Highest Price per Category
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

highest_price = df.groupby('Category')['Price'].max()

print("Highest Price per Category:")
print(highest_price)