import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("03- Pandas/data/sales_data.csv")

plt.figure(figsize=(10,5))

plt.bar(df["Product"], df["Quantity"])

plt.title("Quantity Sold by Product")

plt.xlabel("Product")

plt.ylabel("Quantity Sold")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()