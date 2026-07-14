import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]
plt.figure(figsize=(12,5))
plt.suptitle("Boxplot vs Violinplot")

#boxplot
plt.subplot(1,2,1)

sns.boxplot(
    data=df,
    x="Category",
    y="Revenue",
    color="green"
)
plt.title("Boxplot")
plt.xlabel("Category")
plt.ylabel("Revenue (Rp)")

#violinplot
plt.subplot(1,2,2)
sns.violinplot(
    data=df,
    x="Category",
    y="Revenue",
    color="blue"
)
plt.title("Violin Plot")
plt.xlabel("Category")
plt.ylabel("Revenue (Rp)")

plt.tight_layout(rect=[0,0,1,0.95])

plt.show()