import pandas as pd # Pie Chart
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

category = df.groupby("Category")["Quantity"].sum()

plt.figure(figsize=(6,6))

plt.pie(
    category,
    labels = category.index,
    autopct = "%1.1f%%",
    shadow = True,
    startangle = 90
)

plt.title("Quantity tiap Kategori")

plt.show()