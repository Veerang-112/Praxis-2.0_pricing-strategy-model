# 🛒 Pricing Strategy & Demand Trade-off Exploration  
### 🚀 Retail Analytics | Revenue Strategy | Decision Science

---

## 📌 Overview

This project is an **AI-powered Retail Pricing & Demand Simulation Framework** that enables decision-makers to explore how pricing, discounts, and operational variables influence demand and revenue.

It transforms static pricing decisions into **interactive, data-driven strategic simulations**.

---

## 🎯 Core Capabilities

- 📈 **Demand Prediction Engine** – Machine learning–based demand forecasting  
- 🎯 **Price Elasticity Analysis** – Sensitivity measurement  
- 🔄 **Scenario Simulation** – “What-if” pricing exploration  
- 💰 **Revenue Impact Estimation** – Financial trade-off evaluation  
- 🧠 **Business-Ready Insights** – Strategic, non-technical recommendations  

---

# 🎯 Problem Statement

Retail managers often rely on intuition or static rules when making pricing decisions.

However, pricing directly impacts:

- 📦 Demand  
- 💰 Profit margins  
- 📊 Inventory turnover  
- 🏷 Brand positioning  

This system provides an **interactive decision-support environment** to analyze trade-offs between:

- Price  
- Discount percentage  
- Rating & visibility  
- Delivery time  
- Operational characteristics  

---

# 🏗 Project Architecture

```bash
pricing-strategy-simulator/
│
├── app.py                  # Streamlit interactive dashboard
├── model.py                # ML model training + elasticity logic
├── analysis.py             # Exploratory data analysis
├── requirements.txt
├── pricing_dataset.csv
└── demand_model.pkl        # Generated after model training
```

---

# ⚙️ System Workflow

## 1️⃣ Data Processing

- Load dataset  
- Create derived feature:

```
demand = sold_quantity / (stock + 1)
```

- Select key pricing & operational features  

---

## 2️⃣ Machine Learning Model

We use **XGBoost Regressor** to predict demand based on:

- Final price  
- Discount percentage  
- Rating  
- Number of reviews  
- Delivery time  
- Profit margin  
- Product weight  
- Shelf life  

### 💡 Why XGBoost?

- Handles non-linear pricing behavior  
- Strong performance on structured retail data  
- Robust to feature interactions  

---

## 3️⃣ Price Elasticity Calculation

Elasticity measures how sensitive demand is to price changes.

```
Elasticity = (% change in demand) / (% change in price)
```

### Interpretation Guide

| Elasticity Value | Business Meaning |
|------------------|-----------------|
| < -1 | Highly price sensitive |
| -1 to 0 | Moderately sensitive |
| Close to 0 | Low sensitivity |

---

## 4️⃣ Scenario Simulation Engine

Users can dynamically adjust:

- 🎚 Price  
- 🎟 Discount  
- 🚚 Delivery time  
- ⭐ Rating  

The dashboard instantly recalculates:

- Predicted demand  
- Expected revenue  
- Elasticity  
- Strategic recommendation  

---

# 🚀 Installation & Setup

## 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/your-username/pricing-strategy-simulator.git
cd pricing-strategy-simulator
```

---

## 🔹 Step 2: Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Step 4: Train the Model

```bash
python model.py
```

This generates:

```
demand_model.pkl
```

---

## 🔹 Step 5: Launch the Dashboard

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 📊 Key Features

### ✅ Demand Prediction Engine  
ML-powered real-time demand estimation.

### ✅ Elasticity Analysis  
Understand product-level price sensitivity.

### ✅ Revenue Simulation  
Evaluate short-term pricing impact.

### ✅ Business Narratives  
Executive-friendly strategic insights.

### ✅ Interactive UI  
Dynamic pricing sliders and scenario exploration.

---

# 📈 Business Impact

This tool enables:

- 📌 Smarter pricing decisions  
- 📌 Risk-aware revenue optimization  
- 📌 Category-level strategy comparison  
- 📌 Evidence-based discount planning  

### Example Insight

> Increasing price by 5% in low-elasticity categories can increase revenue without significant demand loss.

---

# 🧠 Hackathon Evaluation Alignment

| Evaluation Criteria | How Addressed |
|--------------------|---------------|
| Actionability | Real pricing recommendations |
| Interpretability | Elasticity explanation |
| Business Realism | Revenue-margin trade-offs |
| Scenario Simulation | Interactive decision support |

---

# 🛠 Tech Stack

- 🐍 Python  
- 📊 Pandas  
- 🔢 NumPy  
- 🚀 XGBoost  
- 🤖 Scikit-learn  
- 🌐 Streamlit  
- 📈 Matplotlib / Seaborn  

---

# 🔮 Future Enhancements

- SHAP Explainability Integration  
- Long-term demand decay modeling  
- Outlet-level pricing optimization  
- Automated PDF strategy reports  
- A/B pricing experimentation module  

---

