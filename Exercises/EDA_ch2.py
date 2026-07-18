import pandas as pd

df = pd.read_csv("Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv")

print("\nTotal Quantity Sold:", df['Quantity'].sum())