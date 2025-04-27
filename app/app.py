import streamlit as st
st.set_page_config(page_title="Price Drop Predictor", layout="centered")

import pandas as pd
import joblib
import numpy as np

# Load model and data
model = joblib.load("price_drop_predictor.pkl")
df = pd.read_csv("cleaned_data.csv")

# Ensure numeric columns are properly converted
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["old_price"] = pd.to_numeric(df["old_price"], errors="coerce")
df["percent_drop"] = pd.to_numeric(df["percent_drop"], errors="coerce")
df = df.dropna(subset=["price", "old_price", "percent_drop", "price_drop"])

# App Title
st.title("🛍️ Price Drop Predictor Dashboard")

# 🔁 Correctly show dropdown using real DataFrame index
product_options = [f"{idx} – {row['title']}" for idx, row in df.iterrows()]
selected = st.selectbox("Select a Product", product_options)

# Extract true index and fetch the row with .loc[]
selected_index = int(selected.split(" – ")[0])
product = df.loc[[selected_index]]  # loc preserves the correct row even if index isn't sequential

# 🏷️ Display product title
st.markdown(f"### 🏷️ Selected Product: `{product['title'].values[0]}`")

# 📊 Predict
features = product[["price", "old_price", "percent_drop"]]
prediction = model.predict(features)[0]
proba = model.predict_proba(features)[0][1]

# 🎯 Compute drop info
drop_amt = round(float(product["old_price"].values[0]) - float(product["price"].values[0]), 2)
drop_pct = float(product["percent_drop"].values[0])
risk = "High" if drop_pct > 40 else "Medium" if drop_pct > 20 else "Low"
recommend = "Wait for Better Deal" if risk != "Low" else "Buy Now"

# 🧾 Output Prediction
st.subheader("📊 Prediction Result")
st.write("**Drop Predicted:**", "Yes" if prediction == 1 else "No")
st.write("**Confidence Score:**", f"{proba:.2f}")
st.write("**Drop Amount:** ₹", drop_amt)
st.write("**Drop %:**", f"{drop_pct:.2f}%")
st.write("**Risk Level:**", risk)
st.write("**Recommendation:**", recommend)

# 📈 Chart 1: Top Categories by Average Drop
st.subheader("📈 Top Categories by Avg. Price Drop")
cat_avg = df.groupby("category")["percent_drop"].mean().sort_values(ascending=False).head(10)
st.bar_chart(cat_avg)

# 📉 Chart 2: Drop Trend Over Time
if "timestamp" in df.columns:
    st.subheader("📉 Drop Trend Over Time")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    trend = df.groupby(df["timestamp"].dt.date)["percent_drop"].mean()
    st.line_chart(trend)
else:
    st.info("ℹ️ No `timestamp` column found for drop trend.")
