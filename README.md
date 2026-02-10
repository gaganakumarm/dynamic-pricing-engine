# **Dynamic Pricing Engine: Revenue-Optimal Pricing Simulator**

[![Streamlit](https://img.shields.io/badge/Live-Dashboard-blue)](https://share.streamlit.io/gaganakumarm/dynamic-pricing-engine/main/app.py)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## **Project Overview**

Retail pricing often relies on heuristics or competitive pricing, leaving revenue on the table.
This project builds an **end-to-end causal pricing optimization engine** that combines:

* Causal Inference (IV & EconML DoubleML) → accurate price elasticity

* Demand simulation & visualization → explore counterfactuals

* Revenue optimization → recommend price that maximizes revenue

The system allows decision-makers to explore **counterfactual scenarios**: “What happens to demand and revenue if we change the price?”

---

## **Live Demo**

**Access the interactive dashboard here:**  [**Launch Interactive Dashboard**](https://share.streamlit.io/gaganakumarm/dynamic-pricing-engine/main/app.py)

**Features in Action:**

| Feature                 | Description                                             |
| ----------------------- | ------------------------------------------------------- |
| Price slider            | Dynamically adjust price to see demand & revenue change |
| Promotion toggle        | Toggle promo ON/OFF and observe elasticity changes      |
| Demand & Revenue curves | Interactive plots highlighting optimal pricing          |
| Optimal price           | Automatically highlighted based on causal elasticity    |

---

## **Key Results**

| Metric                        | Value                                |
| ----------------------------- | ------------------------------------ |
| Baseline Price                | ₹1,035                               |
| Causal Price Elasticity       | −0.262                               |
| Revenue-Maximizing Price      | ₹1,345 (+30%)                        |
| Max Revenue                   | ₹62,737 (22% increase from baseline) |
| Promo vs Non-Promo Elasticity | −0.252 vs −0.265                     |

**Insights:**

1. **Inelastic Demand** → safe price increase
2. **Single-Peaked Revenue Curve** → one clear maximum
3. **Promotions reduce price sensitivity** → optimal price can be higher
4. **Causal inference is essential** → naive OLS/ML overestimates optimal price

---

## **Project Structure**

```
dynamic-pricing-engine/
├── app.py                     # Streamlit dashboard
├── data/
│   ├── simulated/             # Simulated retail dataset (7,300 observations)
├── notebooks/
│   ├── 01_data_simulation.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_demand_modeling.ipynb
│   ├── 04_causal_demand_iv_elasticity.ipynb
│   ├── 05_causal_demand_econml_dml.ipynb
│   ├── 06_revenue_optimal_pricing_simulator.ipynb
├── requirements.txt           # Python dependencies
├── .gitignore
└── README.md
```

---

## **Workflow / Methodology**

### **Phase 1 — Data Simulation**

* Simulated 20 retail products × 365 days
* Added **price, demand, promotion, and seasonality features**

### **Phase 2 — Exploratory Data Analysis**

* Analyzed **distributions, correlations, seasonality**, and **promotions effects**
* Identified endogeneity in price → naive OLS insufficient

### **Phase 3 — Demand Modeling**

* Built **naive OLS**, **log–log OLS**, and **Gradient Boosting ML** models
* Highlighted difference between **prediction vs causal estimation**

### **Phase 4 — Causal Elasticity**

* Applied **Instrumental Variables (IV)** and **EconML LinearDML**
* Estimated **causal price elasticity**: ~−0.262
* Compared **promo vs non-promo scenarios**

### **Phase 5 — Revenue Optimization**

* Defined **price-demand relationship** using causal elasticity
* Built **revenue function** and simulated **price grid**
* Identified **revenue-maximizing price**: ₹1,345 (+30% from baseline)

### **Phase 6 — Streamlit Dashboard**

* Interactive **price slider & promotion toggle**
* Dynamic **demand & revenue curves**
* Highlights **optimal price** for actionable recommendations

---

## **Technologies Used**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![EconML](https://img.shields.io/badge/EconML-FF6F61?style=for-the-badge&logo=python&logoColor=white)](https://econml.azurewebsites.net/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

---

## **Getting Started**

Clone the repo:

```bash
git clone https://github.com/gaganakumarm/dynamic-pricing-engine.git
cd dynamic-pricing-engine
```

Create virtual environment and install dependencies:

```bash
python -m venv pricing-env
pricing-env\Scripts\activate      # Windows
pip install -r requirements.txt
```

Run Streamlit dashboard locally:

```bash
streamlit run app.py
```

