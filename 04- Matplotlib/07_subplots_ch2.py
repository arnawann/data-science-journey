import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))
plt.suptitle("Sales Dashboard", fontsize=18)

#Grafik pertama-Bar Chart Revenue

plt.subplot(2,2,1)
plt.bar(df["Product"], df["Revenue"], color="orange")
plt.title("Revenue by Product")
plt.xticks(rotation=45)

#Grafik kedua-Line Chart Revenue

plt.subplot(2,2,2)
plt.plot(
    df["Product"],
    df["Revenue"],
    color="gray",
    marker="o"
)
plt.title("Revenue Trend")
plt.xticks(rotation=45)

#Grafik ketiga-Scatter Plot

plt.subplot(2,2,3)
plt.scatter(df["Quantity"], df["Revenue"])
plt.title("Quantity vs Revenue")
plt.xticks(rotation=45)

#Grafik keempat-Histogram Quantity

plt.subplot(2,2,4)
plt.hist(df["Quantity"])
plt.title("Distribution of Product Quantity")

plt.tight_layout()
plt.show()
         
