#Materi 4 — Count Products per Category
import pandas as pd
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

count_product = df.groupby('Category')['Products'].count()

print(count_product)