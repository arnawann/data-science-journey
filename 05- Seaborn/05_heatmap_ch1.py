import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")
df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(6,5))

numeric = df[["Price", "Quantity", "Revenue"]]

corr = numeric.corr()
print(corr)

sns.heatmap(
    corr,
    annot=True,
    cmap="Greens",
    linewidths=1,
    linecolor="white"
)
plt.title("Correlation Matrix")
plt.show()