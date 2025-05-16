import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("model.pkl")

# Set page config
st.set_page_config(page_title="House Price Predictor 🏠", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #F4F6F7;
    }
    .stButton button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stNumberInput > div > input {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.title("🏡 Indian House Price Predictor")
st.write("Use machine learning to estimate house prices based on your inputs.")

st.divider()

# Inputs
bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=0, value=2)
bathrooms = st.number_input("🛁 Number of Bathrooms", min_value=0, value=2)
livingarea = st.number_input("📏 Living Area (sqft)", min_value=0, value=2000)
condition = st.number_input("🏠 Condition of House (0-5)", min_value=0, max_value=5, value=3)
numberofschools = st.number_input("🏫 Number of Schools Nearby", min_value=0, value=2)

st.divider()

# Prediction
X = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]

if st.button("🚀 Predict Now!"):
    st.balloons()
    prediction = model.predict(np.array(X))
    st.success(f"💰 Estimated House Price: ₹ {float(prediction):,.2f}")
else:
    st.info("Enter all values and hit Predict!")
