import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("pricing_dataset.csv")
df.columns = df.columns.str.strip()

print("✅ Dataset Loaded Successfully\n")

# -----------------------------
# Data Cleaning
# -----------------------------
df["discounted_price"] = df["discounted_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["actual_price"] = df["actual_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(float)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["rating_count"] = df["rating_count"].str.replace(",", "").astype(float)

df = df.dropna()

# -----------------------------
# Feature Engineering
# -----------------------------
df["profit_margin"] = df["discounted_price"] - df["actual_price"]

# Demand Proxy (since no real sales data)
df["demand_proxy"] = df["rating_count"]

print("✅ Data Cleaned Successfully\n")

# -----------------------------
# Basic Info
# -----------------------------
print("📊 Dataset Info:")
print(df.info())

print("\n📈 Summary Statistics:")
print(df.describe())

# -----------------------------
# Correlation Analysis
# -----------------------------
print("\n🔍 Correlation Matrix:")
corr = df[[
    "discounted_price",
    "actual_price",
    "discount_percentage",
    "rating",
    "rating_count",
    "profit_margin"
]].corr()

print(corr)

plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# Price vs Demand Analysis
# -----------------------------
plt.figure()
sns.scatterplot(x="discounted_price", y="demand_proxy", data=df)
plt.title("Price vs Demand Proxy")
plt.xlabel("Discounted Price")
plt.ylabel("Rating Count (Demand Proxy)")
plt.show()

# -----------------------------
# Discount Impact
# -----------------------------
plt.figure()
sns.scatterplot(x="discount_percentage", y="demand_proxy", data=df)
plt.title("Discount % vs Demand Proxy")
plt.show()

# -----------------------------
# Category-Level Analysis
# -----------------------------
if "category" in df.columns:
    category_summary = df.groupby("category")["demand_proxy"].mean().sort_values(ascending=False)

    print("\n🏷 Category-wise Average Demand:")
    print(category_summary.head())

    plt.figure()
    category_summary.head(10).plot(kind="bar")
    plt.title("Top 10 Categories by Demand Proxy")
    plt.ylabel("Average Demand Proxy")
    plt.show()

# -----------------------------
# Elasticity Approximation
# -----------------------------
df["price_change"] = df["discounted_price"].pct_change()
df["demand_change"] = df["demand_proxy"].pct_change()

df["elasticity"] = df["demand_change"] / df["price_change"]

elasticity_mean = df["elasticity"].replace([np.inf, -np.inf], np.nan).dropna().mean()

print("\n📉 Average Price Elasticity:", round(elasticity_mean, 2))

# -----------------------------
# Business Insight Summary
# -----------------------------
print("\n🧠 Business Insights:")

if elasticity_mean < -1:
    print("Demand is highly price sensitive across products.")
elif -1 <= elasticity_mean < 0:
    print("Demand shows moderate price sensitivity.")
else:
    print("Demand appears relatively inelastic.")

high_discount = df[df["discount_percentage"] > 50]["demand_proxy"].mean()
low_discount = df[df["discount_percentage"] < 20]["demand_proxy"].mean()

print("\nAverage Demand at High Discount (>50%):", round(high_discount, 2))
print("Average Demand at Low Discount (<20%):", round(low_discount, 2))

print("\n✅ Analysis Completed Successfully")
