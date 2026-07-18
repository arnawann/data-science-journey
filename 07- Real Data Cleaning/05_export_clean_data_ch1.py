import pandas as pd #CH1-Export the dataset without an index.

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

df.to_csv(
    "07- Real Data Cleaning/cleaned_sales_data.csv",
    index=False
)

print("Your dataset exported successfully!")