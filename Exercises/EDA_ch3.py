import pandas as pd

df = pd.read_csv("Project-02-Exploratory-Data-Analysis/data/cleaned_sales_data.csv")

idx = df['Price'].idxmax()

print("\nMost Expensive Product:") 
print(df.loc[idx, 'Product'])

print('Price:')
print(df.loc[idx,'Price'])