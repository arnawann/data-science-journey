import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("03- Pandas/data/sales_data.csv")

plt.figure(figsize=(10,5))

plt.bar(df["Product"], df["Price"])

plt.title("Price by Product")

plt.xlabel("Product")

plt.ylabel("Price (Rp)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()