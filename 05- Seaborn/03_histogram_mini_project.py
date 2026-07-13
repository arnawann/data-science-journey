import pandas as pd #Mini Project buat dua histogram berdampingan.
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))
plt.suptitle("Histogram", fontsize=18)

#Histogram1
plt.subplot(1,2,1)

sns.histplot(
    data=df,
    x="Price",
    color="yellow",
    kde=True
)
plt.title("Distribution of Price")

#Histogram2
plt.subplot(1,2,2)

sns.histplot(
    data=df,
    x="Revenue",
    color="green",
    kde=True
)

plt.title("Distribution of Revenue")

plt.tight_layout()

plt.show()