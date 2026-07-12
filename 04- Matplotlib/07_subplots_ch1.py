import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))

#grafik pertama

plt.subplot(1,2,1)
plt.bar(df["Product"], df["Revenue"], color="green")

plt.title("Revenue by Product")

plt.xticks(rotation=45)

#grafik kedua

plt.subplot(1,2,2)

plt.plot(
    df["Product"],
    df["Revenue"],
    color="yellow",
    marker="o"
)

plt.title("Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()