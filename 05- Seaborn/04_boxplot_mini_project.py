import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")
df["Revenue"] = df["Price"] * df["Quantity"]
plt.figure(figsize=(12,5))
plt.suptitle("Sales Dashboard", fontsize=18)

#boxplot1
plt.subplot(1,2,1)

sns.boxplot(
    data=df,
    y="Price",
    color="purple"
)
plt.title("Distribution of Price")

#boxplot2
plt.subplot(1,2,2)

sns.boxplot(
    data=df,
    x="Category",
    y="Revenue",
    color="red"
)

plt.title("Revenue by Category")
plt.show()