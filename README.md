# Praxis-2.0
🛒 Pricing Strategy & Demand Trade-off Exploration
📌 Overview

This project is a Retail Pricing & Demand Simulation Framework designed to help decision-makers explore how pricing, discounts, and operational factors impact product demand and revenue.

The system enables:

📈 Demand prediction under different pricing conditions

🎯 Price elasticity analysis

🔄 Scenario simulation (“What if price increases?”)

💰 Revenue impact comparison

🧠 Business-ready strategic recommendations

Built for hackathon-level business analytics and decision science applications.

🎯 Problem Statement

Retail managers often rely on static rules or intuition while making pricing decisions. However, pricing influences:

Demand

Profit margins

Inventory flow

Brand perception

This project provides an interactive simulation environment to analyze trade-offs between:

Price

Discount

Visibility factors

Delivery time

Ratings

🏗 Project Architecture
pricing_strategy_project/
│
├── app.py                  # Streamlit interactive dashboard
├── model.py                # ML model training + elasticity logic
├── analysis.py             # Exploratory data analysis
├── requirements.txt
├── pricing_dataset.csv
└── demand_model.pkl        # Generated after model training

⚙️ How It Works
1️⃣ Data Processing

Load dataset

Create derived feature:

demand = sold_quantity / (stock + 1)


Select relevant pricing & operational features

2️⃣ Machine Learning Model

We use XGBoost Regressor to predict demand based on:

Final price

Discount percentage

Rating

Number of reviews

Delivery time

Profit margin

Weight

Shelf life

Why XGBoost?

Handles non-linear relationships

High accuracy

Robust for structured retail data

3️⃣ Price Elasticity Calculation

Elasticity measures how sensitive demand is to price changes.

Formula used:

Elasticity = (% change in demand) / (% change in price)


Interpretation:

Elasticity	Meaning
< -1	Highly price sensitive
Between -1 and 0	Moderately sensitive
Close to 0	Low sensitivity
4️⃣ Scenario Simulation

Users can modify:

Price

Discount

Delivery time

Rating

The app instantly recalculates:

Predicted demand

Expected revenue

Elasticity

Strategic recommendation

🚀 Installation & Setup
Step 1: Clone Repository
git clone https://github.com/your-username/pricing-strategy-simulator.git
cd pricing-strategy-simulator

Step 2: Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Train the Model
python model.py


This will generate:

demand_model.pkl

Step 5: Run the Application
streamlit run app.py


Open browser at:

http://localhost:8501

📊 Key Features
✅ Demand Prediction Engine

ML-powered demand estimation.

✅ Elasticity Analysis

Understand price sensitivity per product category.

✅ Revenue Estimation

Simulate short-term financial impact.

✅ Business Narratives

Non-technical strategic suggestions.

✅ Interactive Dashboard

Real-time simulation via Streamlit.

📈 Business Value

This tool enables:

Smarter pricing decisions

Risk-aware revenue planning

Category-level strategy optimization

Evidence-based discount planning

Example Insight:

Increasing price by 5% in low-elasticity categories increases revenue without significant demand drop.

🧠 Evaluation Alignment

This solution satisfies hackathon evaluation criteria:

Criteria	How Addressed
Actionability	Real pricing recommendations
Interpretability	Elasticity explanation
Business realism	Revenue & margin trade-offs
Scenario simulation	Interactive decision support
🛠 Tech Stack

Python

Pandas

NumPy

XGBoost

Scikit-learn

Streamlit

Matplotlib / Seaborn

🔮 Future Enhancements

SHAP explainability integration

Long-term demand decay modeling

Outlet-level pricing optimization

Automated strategic reports (PDF export)

A/B pricing simulation
