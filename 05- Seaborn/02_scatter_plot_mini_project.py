import pandas as pd #buat dua grafik scatter plot dari matplotlib dan seaborn bersandingan
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]


plt.figure(figsize=(12,5))
plt.suptitle("Sales Dashboard",fontsize=18)

#matplotlib
plt.subplot(1,2,1)

plt.scatter(
    df["Price"],
    df["Revenue"],
    color="blue"
)

plt.title("Matplotlib")
plt.xlabel("Price")
plt.ylabel("Revenue")

#seaborn
plt.subplot(1,2,2)

sns.scatterplot(
    data=df,
    x="Price",
    y="Revenue",
    color="Green",
    marker="o"
)

plt.title("Seaborn")
plt.xlabel("Price")
plt.ylabel("Revenue")

plt.tight_layout()

plt.show()