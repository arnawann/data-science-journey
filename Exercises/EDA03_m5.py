#Materi 5 — Multiple Aggregation
import pandas as pd
df = pd.read_csv(
    "Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv"
)

df['Revenue'] = df['Price'] * df['Quantity']

summary = df.groupby('Category').agg({
    'Price':'mean',
    'Quantity':'mean',
    'Revenue':'sum'
})

print(summary)