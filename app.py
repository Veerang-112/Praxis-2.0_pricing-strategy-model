import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("demand_model.pkl")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("pricing_dataset.csv")
df.columns = df.columns.str.strip()

# Clean dataset same as model.py
df["discounted_price"] = df["discounted_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["actual_price"] = df["actual_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(float)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["rating_count"] = df["rating_count"].str.replace(",", "").astype(float)

df = df.dropna()

# -----------------------------
# Streamlit UI
# -----------------------------

st.title("🛒 Pricing Strategy & Demand Simulator")
st.markdown("Explore how pricing decisions impact demand and revenue.")

st.sidebar.header("📊 Scenario Controls")

price = st.sidebar.slider(
    "Discounted Price (₹)",
    int(df["discounted_price"].min()),
    int(df["discounted_price"].max()),
    int(df["discounted_price"].mean())
)

actual_price = st.sidebar.slider(
    "Actual Price (₹)",
    int(df["actual_price"].min()),
    int(df["actual_price"].max()),
    int(df["actual_price"].mean())
)

discount = st.sidebar.slider(
    "Discount Percentage (%)",
    0,
    90,
    int(df["discount_percentage"].mean())
)

rating = st.sidebar.slider(
    "Product Rating",
    1.0,
    5.0,
    float(df["rating"].mean())
)

# -----------------------------
# Feature Engineering
# -----------------------------
profit_margin = price - actual_price

input_data = pd.DataFrame([[
    price,
    actual_price,
    discount,
    rating,
    profit_margin
]], columns=[
    "discounted_price",
    "actual_price",
    "discount_percentage",
    "rating",
    "profit_margin"
])

# -----------------------------
# Prediction
# -----------------------------
predicted_demand = model.predict(input_data)[0]

# Revenue Calculation
predicted_revenue = predicted_demand * price

# -----------------------------
# Elasticity Approximation
# -----------------------------
price_change = 0.05 * price
new_price = price + price_change

new_profit_margin = new_price - actual_price

new_input = pd.DataFrame([[
    new_price,
    actual_price,
    discount,
    rating,
    new_profit_margin
]], columns=input_data.columns)

new_demand = model.predict(new_input)[0]

elasticity = ((new_demand - predicted_demand) / predicted_demand) / (price_change / price)

# -----------------------------
# Display Results
# -----------------------------
st.subheader("📈 Simulation Results")

st.metric("Predicted Demand (Proxy)", int(predicted_demand))
st.metric("Estimated Revenue (₹)", int(predicted_revenue))
st.metric("Price Elasticity", round(elasticity, 2))

# -----------------------------
# Business Recommendation
# -----------------------------
st.subheader("🧠 Strategic Recommendation")

if elasticity < -1:
    st.warning("Demand is highly price sensitive. Increasing price may significantly reduce demand.")
elif -1 <= elasticity < 0:
    st.info("Demand is moderately sensitive. Small price changes can be optimized.")
else:
    st.success("Demand is relatively inelastic. Price increase may improve revenue.")

st.markdown("""
### 📌 Insight:
We use **rating_count as a demand proxy**, since real sales data was not available.
Higher review volume typically correlates with higher product sales in e-commerce.
""")
