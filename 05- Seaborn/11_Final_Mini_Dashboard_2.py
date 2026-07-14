import pandas as pd #Final Mini Dashboard 2
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette("pastel")

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,8))

plt.suptitle(
    "Sales Dashboard 2",
    fontsize=18,
    fontweight="bold"
)

#Scatter Plot
plt.subplot(2,2,1)

sns.scatterplot(
    data=df,
    x="Price",
    y="Revenue"
)
plt.title("Price vs Revenue")
plt.xlabel("Price")
plt.ylabel("Revenue (Rp)")

#Heatmap
plt.subplot(2,2,2)

corr = df[
    ["Price", "Quantity", "Revenue"]
].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues",
    linewidths=1,
    linecolor="white"
)
plt.title("Correlation Matrix")

#Violinplot
plt.subplot(2,2,3)
sns.violinplot(
    data=df,
    x="Category",
    y="Revenue"
)
plt.title("Revenue Distribution")
plt.xlabel("Category")
plt.ylabel("Revenue (Rp)")

#Boxplot
plt.subplot(2,2,4)
sns.boxplot(
    data=df,
    x="Category",
    y="Revenue"
)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (Rp)")

plt.tight_layout()
plt.show()