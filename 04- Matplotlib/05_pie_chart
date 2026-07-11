import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

category = df.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(6,6))

plt.pie(
    category,
    labels=category.index,
    autopct="%1.1f%%"
)

plt.title("Revenue by Category")

plt.show()