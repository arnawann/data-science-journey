#CH3 - Display print(clean_df.info()) to make sure there are no more missing values.

import pandas as pd

clean_df = pd.read_csv(
    "07- Real Data Cleaning/cleaned_sales_data.csv"
)

print(clean_df.info())