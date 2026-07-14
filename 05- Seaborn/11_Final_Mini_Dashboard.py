import pandas as pd #Final Mini Dashboard 1
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette("Set2")

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,8))

plt.suptitle(
    "Sales Dashboard 1",
    fontsize=18,
    fontweight="bold"
)

#Revenue by Product (Barplot)
plt.subplot(2,2,1)

sns.barplot(
    data=df,
    x="Product",
    y="Revenue"
)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rp)")

#Revenue Trend (Lineplot)
plt.subplot(2,2,2)

sns.lineplot(
    data=df,
    x="Product",
    y="Revenue",
    marker="o"
)
plt.title("Revenue Trend")
plt.xlabel("Product")
plt.ylabel("Revenue (Rp)")
plt.xticks(rotation=45)

#Price Distribution (Histogram)
plt.subplot(2,2,3)

sns.histplot(
    data=df,
    x="Price",
    bins=5
)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

#Correlation Matrix (Heatmap)
plt.subplot(2,2,4)

numeric = df[["Price", "Quantity", "Revenue"]]

corr = numeric.corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues",
    linewidths=1,
    linecolor="white"
)
plt.title("Correlation Matrix")

plt.tight_layout()
plt.show()