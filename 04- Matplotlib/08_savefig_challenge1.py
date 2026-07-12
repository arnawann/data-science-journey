#buat bar chart revenue simpan jadi revenue_bar.png

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))

plt.bar(
    df["Product"], 
    df["Revenue"], 
       color="yellow"
)

plt.title("Revenue by Product")

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("04- Matplotlib/revenue_bar.png")
plt.show()

