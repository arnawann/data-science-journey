import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")
df["Revenue"] = df["Price"] * df["Quantity"]
plt.figure(figsize=(12,5))
plt.suptitle("Sales Dashboard", fontsize=18)

#Grafik pertama-Bar Chart Revenue

plt.subplot(2,2,1)
plt.bar(df["Product"], df["Revenue"], color="brown")
plt.title("Revenue by Product")
plt.xticks(rotation=45)

#Grafik kedua-Quantity Trend (Line)

plt.subplot(2,2,2)
plt.plot(
    df["Product"],
    df["Quantity"],
    color="red",
    marker="o"
)
plt.title("Quantity Trend")
plt.xticks(rotation=45)
plt.tight_layout()

#Grafik ketiga-Price Distribution (Histogram)

plt.subplot(2,2,3)
plt.hist(df["Price"], color="blue", edgecolor="black") 
plt.title("Distribution of Price")

#Grafik keempat-Revenue by Category (Pie)

plt.subplot(2,2,4)
category = df.groupby("Category")["Revenue"].sum()
plt.pie(
    category,
    labels=category.index,
    autopct="%1.1f%%"
)
plt.title("Revenue by Category")
plt.show()