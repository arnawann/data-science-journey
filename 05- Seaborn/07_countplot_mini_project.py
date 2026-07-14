import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]
plt.figure(figsize=(12,5))
plt.suptitle("Bar Chart Matplotlib vs Countplot Seaborn", fontsize=16)

#bar chart matplotlib
plt.subplot(1,2,1)

category_count = df["Category"].value_counts()
plt.bar(
    category_count.index, 
    category_count.values,
    color='green'
)

plt.title("Matplotlib")

#countplot seaborn
plt.subplot(1,2,2)

sns.countplot(
    data=df,
    x="Category",
    color='red'
)

plt.title("Seaborn")

plt.tight_layout()

plt.show()
