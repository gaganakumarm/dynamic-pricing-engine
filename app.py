import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dynamic Pricing Simulator", layout="wide")

# ---------- HEADER ----------
st.title("Revenue-Optimal Pricing Simulator")
st.caption("Causal Demand Modeling • Price Elasticity • Revenue Optimization")

# ---------- LOAD BASELINE PARAMETERS ----------
df = pd.read_csv(
    "data/simulated/retail_pricing_data.csv",
    parse_dates=["date"]
)

p0 = df["price"].mean()  # Baseline price from data
q0 = df["demand"].mean()  # Baseline demand from data

# ---------- SIDEBAR ----------
st.sidebar.header("Controls")

price = st.sidebar.slider(
    "Set Price (₹)",
    min_value=int(0.7 * p0),
    max_value=int(1.3 * p0),
    value=int(p0),
    step=10
)

promo = st.sidebar.toggle("Promotion Active", value=False)

# ---------- REAL CAUSAL ELASTICITY ----------
ELASTICITY_PROMO_ON = -0.252
ELASTICITY_PROMO_OFF = -0.265
elasticity = ELASTICITY_PROMO_ON if promo else ELASTICITY_PROMO_OFF

REFERENCE_PRICE = p0
BASE_DEMAND = q0

# ---------- CURRENT PRICE SCENARIO ----------
promo_multiplier = 1.12 if promo else 1.0

demand = BASE_DEMAND * (price / REFERENCE_PRICE) ** elasticity
demand = max(demand, 0) * promo_multiplier
revenue = price * demand

# ---------- REVENUE CURVE + OPTIMAL PRICE FINDER ----------
price_grid = np.linspace(0.7 * p0, 1.3 * p0, 200)

demand_curve = BASE_DEMAND * (price_grid / REFERENCE_PRICE) ** elasticity
demand_curve = demand_curve * 1.12 if promo else demand_curve

revenue_curve = price_grid * demand_curve

optimal_idx = np.argmax(revenue_curve)
optimal_price = price_grid[optimal_idx]
optimal_revenue = revenue_curve[optimal_idx]

# ---------- METRICS ----------
col1, col2, col3 = st.columns(3)

col1.metric("Current Price", f"₹{int(price)}")
col2.metric("Estimated Demand", f"{int(demand)} units")
col3.metric("Revenue", f"₹{int(revenue):,}")

# ---------- ELASTICITY TRANSPARENCY ----------
st.write(
    f"**Elasticity used:** {elasticity} "
    f"({'Promo ON' if promo else 'Promo OFF'})"
)

# ----------  VISUALS (INTERVIEW GOLD) ----------
st.subheader(" Demand & Revenue Curves")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Demand curve
ax1.plot(price_grid, demand_curve, linewidth=2.5, color="#1f77b4", label="Demand")
ax1.axvline(price, linestyle="-", linewidth=2, color="#ff7f0e", alpha=0.7, label="Current Price")
ax1.axvline(optimal_price, linestyle="--", linewidth=2, color="#2ca02c", label="Optimal Price")
ax1.set_xlabel("Price (₹)", fontsize=11, fontweight="bold")
ax1.set_ylabel("Demand (units)", fontsize=11, fontweight="bold")
ax1.set_title("Demand Curve", fontsize=12, fontweight="bold")
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_ylim(bottom=0)  # Remove negatives

# Revenue curve
ax2.plot(price_grid, revenue_curve, linewidth=2.5, color="#d62728", label="Revenue")
ax2.axvline(price, linestyle="-", linewidth=2, color="#ff7f0e", alpha=0.7, label="Current Price")
ax2.axvline(optimal_price, linestyle="--", linewidth=2, color="#2ca02c", label="Optimal Price")
ax2.text(optimal_price, np.max(revenue_curve) * 0.9, "  Optimal\n  Price", 
         rotation=0, fontsize=9, fontweight="bold", color="#2ca02c")
ax2.set_xlabel("Price (₹)", fontsize=11, fontweight="bold")
ax2.set_ylabel("Revenue (₹)", fontsize=11, fontweight="bold")
ax2.set_title("Revenue Curve", fontsize=12, fontweight="bold")
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_ylim(bottom=0)

plt.tight_layout()
st.pyplot(fig, use_container_width=True)

impact = "Higher optimal price under promotion" if promo else "Baseline price sensitivity"

st.success(
    f"**Optimal Price:** ₹{int(optimal_price):,} | "
    f"**Max Revenue:** ₹{int(optimal_revenue):,} | "
    f"**{impact}**"
)

# ---------- CAUSAL CONTEXT ----------
st.info(
    "This simulator uses **causal price elasticity** (DML) to estimate "
    "counterfactual demand and revenue under price changes."
)
