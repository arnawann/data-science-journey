import pandas as pd # Challenge 1 Buat Box Plot: Price warna biru
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

sns.boxplot(
    data=df,
    y="Price",
    color="blue"
)

plt.title("Distribution of Product Prices")
plt.show()