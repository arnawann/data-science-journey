import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

plt.figure(figsize=(8,5))

plt.hist(df["Price"])

plt.title("Distribution of Product Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()