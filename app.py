import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Pricing Strategy Simulator", layout="wide")

model = joblib.load("demand_model.pkl")
df = pd.read_csv("pricing_dataset.csv")

df["demand"] = df["sold_quantity"] / (df["stock"] + 1)

st.title("🛒 Pricing & Demand Trade-off Simulator")

# ---- Sidebar Controls ----
st.sidebar.header("Scenario Inputs")

category = st.sidebar.selectbox("Category", df["category"].unique())
sample = df[df["category"] == category].iloc[0]

price = st.sidebar.slider(
    "Final Price",
    float(sample["final_price"] * 0.5),
    float(sample["final_price"] * 1.5),
    float(sample["final_price"])
)

discount = st.sidebar.slider("Discount %", 0, 60, int(sample["discount_pct"]))
delivery = st.sidebar.slider("Delivery Time (min)", 5, 90, int(sample["delivery_time_min"]))
rating = st.sidebar.slider("Rating", 1.0, 5.0, float(sample["rating"]))

input_data = {
    "final_price": price,
    "discount_pct": discount,
    "rating": rating,
    "num_reviews": sample["num_reviews"],
    "delivery_time_min": delivery,
    "profit_margin_pct": sample["profit_margin_pct"],
    "weight_g": sample["weight_g"],
    "shelf_life_days": sample["shelf_life_days"]
}

pred_demand = model.predict(pd.DataFrame([input_data]))[0]

revenue = price * pred_demand

# ---- Outputs ----
st.metric("📦 Predicted Demand Index", round(pred_demand, 3))
st.metric("💰 Expected Revenue", f"₹ {round(revenue,2)}")

# ---- Elasticity ----
base = input_data.copy()
base_price = base["final_price"]
base_demand = pred_demand

base["final_price"] = base_price * 1.05
new_demand = model.predict(pd.DataFrame([base]))[0]

elasticity = ((new_demand - base_demand) / base_demand) / 0.05

st.subheader("📉 Price Elasticity")
st.write(round(elasticity, 2))

if elasticity < -1:
    st.error("Highly price sensitive → avoid price hikes")
else:
    st.success("Low price sensitivity → price increase possible")

# ---- Business Summary ----
st.subheader("🧠 Strategic Recommendation")

if discount > 30 and pred_demand < 0.2:
    st.warning("High discount but weak demand → visibility or delivery issue")
elif price < sample["final_price"]:
    st.success("Lower price improves volume but margin trade-off exists")
else:
    st.info("Balanced pricing with sustainable demand")
