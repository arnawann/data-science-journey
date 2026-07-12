import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))

# Grafik pertama

plt.subplot(1,2,1)

plt.bar(df["Product"], df["Revenue"], color="skyblue")

plt.title("Revenue by Product")

plt.xticks(rotation=45)

# Grafik kedua

plt.subplot(1,2,2)

plt.plot(
    df["Product"],
    df["Revenue"],
    color="red",
    marker="o"
)

plt.title("Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()