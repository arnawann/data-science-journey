import pandas as pd #CH2-Review the exported file.

clean_df = pd.read_csv(
    "07- Real Data Clean/cleaned_sales_data.csv"
)

print(clean_df)
