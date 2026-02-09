# 🛒 Pricing Strategy & Demand Trade-off Exploration

## 📌 Overview

This project is a **Retail Pricing & Demand Simulation Framework** designed to help decision-makers explore how pricing decisions impact product demand and revenue.

Since direct sales data was not available in the dataset, we use **review volume (`rating_count`) as a demand proxy**, a common analytical practice in e-commerce platforms.

The system enables:

- 📈 Demand prediction under different pricing conditions  
- 🎯 Price elasticity analysis  
- 🔄 Scenario simulation (“What if price increases?”)  
- 💰 Revenue impact comparison  
- 🧠 Business-ready strategic recommendations  

Built as a hackathon-level **Retail Analytics & Decision Science prototype**.

---

## 🎯 Problem Statement

Retail managers often rely on static rules or intuition while making pricing decisions. However, pricing influences:

- Demand
- Profit margins
- Brand perception
- Revenue performance

This project provides an interactive simulation environment to analyze trade-offs between:

- Discounted Price  
- Actual Price  
- Discount Percentage  
- Ratings  
- Profit Margins  

---

## 📊 Dataset Adaptation

The updated dataset does **not include direct sales or stock data**.

Therefore:

### 🔁 Demand Proxy Used:
```
rating_count → Proxy for product demand
```

Why?

Higher number of reviews generally correlates with higher product sales on e-commerce platforms.

This ensures:

- Business realism  
- Analytical validity  
- Practical interpretability  

---

## 🏗 Project Architecture

```
pricing_strategy_project/
│
├── app.py                  # Streamlit interactive dashboard
├── model.py                # ML model training + elasticity logic
├── pricing_dataset.csv     # Hackathon dataset
├── demand_model.pkl        # Generated after model training
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Data Processing

- Cleans ₹ symbols and percentage signs
- Converts text values to numeric
- Removes missing values
- Creates derived feature:

```
profit_margin = discounted_price - actual_price
```

---

### 2️⃣ Machine Learning Model

We use:

```
XGBoost Regressor
```

### Features Used:

- discounted_price
- actual_price
- discount_percentage
- rating
- profit_margin

### Target:

```
rating_count (Demand Proxy)
```

Why XGBoost?

- Handles non-linear pricing effects
- Robust for structured retail data
- High predictive performance

---

### 3️⃣ Price Elasticity Calculation

Elasticity measures demand sensitivity to price changes.

Formula:

```
Elasticity = (% change in demand) / (% change in price)
```

Interpretation:

| Elasticity | Meaning |
|------------|----------|
| < -1 | Highly price sensitive |
| -1 to 0 | Moderately sensitive |
| Close to 0 | Low sensitivity (inelastic) |

---

### 4️⃣ Scenario Simulation

Users can modify:

- Discounted Price  
- Actual Price  
- Discount Percentage  
- Rating  

The app instantly recalculates:

- 📈 Predicted Demand  
- 💰 Estimated Revenue  
- 🎯 Price Elasticity  
- 🧠 Strategic Recommendation  

---

## 🚀 Installation & Setup

### Step 1: Clone Repository

```
git clone https://github.com/your-username/pricing-strategy-simulator.git
cd pricing-strategy-simulator
```

---

### Step 2: Create Virtual Environment

**Windows**
```
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**
```
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 4: Train the Model

```
python model.py
```

This generates:

```
demand_model.pkl
```

---

### Step 5: Run the Application

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📈 Key Features

✅ Demand Prediction Engine (ML-based)

✅ Elasticity Analysis

✅ Revenue Simulation

✅ Business Recommendation Logic

✅ Interactive Dashboard (Streamlit)

---

## 🧠 How ML + Analytics Were Used

| Component | Usage |
|------------|--------|
| Machine Learning | Demand prediction using XGBoost |
| Feature Engineering | Profit margin creation |
| Elasticity Modeling | Sensitivity measurement |
| Scenario Simulation | Real-time decision testing |

---

## 💼 Business Value

This tool enables:

- Smarter pricing decisions  
- Revenue optimization  
- Discount impact evaluation  
- Risk-aware price adjustments  

Example Insight:

> If elasticity is low, price increase may improve revenue without significant demand drop.

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- XGBoost  
- Scikit-learn  
- Streamlit  

---

## 🔮 Future Enhancements

- SHAP Explainability
- Category-level comparison
- Revenue heatmaps
- Automated PDF strategy reports
- A/B pricing simulations

---

## 📌 Hackathon Evaluation Alignment

| Criteria | How Addressed |
|------------|--------------|
| Actionability | Real pricing recommendations |
| Interpretability | Elasticity explanation |
| Business realism | Revenue + margin trade-offs |
| Scenario simulation | Interactive decision support |

---

## 👨‍💻 Developed For

Retail Analytics | Revenue Strategy | Decision Science Hackathon
