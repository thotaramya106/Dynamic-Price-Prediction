import streamlit as st
import pickle
import pandas as pd

# Load regression model
with open("model_rf.pkl", "rb") as file:
    model_rf = pickle.load(file)

st.title(" Dynamic Price Prediction App")

# Feature: Expected Ride Duration
expected_ride_duration = st.number_input(
    "Expected Ride Duration (minutes)",
    min_value=1,
    max_value=500,
    value=60
)

# Feature: Cost Category
cost_category_options = ["Low", "Medium", "High", "Very High"]
cost_category = st.selectbox("Cost Category", cost_category_options)

# Predict button
if st.button("Predict Dynamic Price"):
    input_data = pd.DataFrame([{
        "Expected_Ride_Duration": expected_ride_duration,
        "Cost_Category": cost_category
    }])

    prediction = model_rf.predict(input_data)[0]

    st.success(f"Predicted Dynamic Price: ₹{prediction:.2f}")
