import streamlit as st
import pandas as pd
import numpy as np
import joblib

# === Load Trained Model ===
model = joblib.load(
    r"C:\Users\USER\Desktop\Uni lvl 200\Project Repository\Diabetes predictor app\model\diabetes_model.pkl")


# === Risk Categorization Function ===
def get_risk_level(prob):
    if prob >= 0.85:
        return "High"
    elif prob >= 0.6:
        return "Medium"
    elif prob >= 0.4:
        return "Low"
    else:
        return "Normal"


# === Streamlit UI ===
st.set_page_config(page_title="Diabetes Risk Predictor", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🩺 Diabetes Risk Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your health metrics below to predict your diabetes risk level.</p>",
            unsafe_allow_html=True)

# === User Input ===
with st.form("input_form"):
    name = st.text_input("👤 Your Name", max_chars=50)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=0.0)
    age = st.number_input("Age", min_value=0, step=1)
    bmi = st.number_input("BMI", min_value=0.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5)
    insulin = st.number_input("Insulin Level (µU/mL)", min_value=0.0)
    submitted = st.form_submit_button("Predict")

# === Prediction Logic ===
if submitted:
    input_data = np.array([[glucose, age, bmi, dpf, insulin]])

    prob = model.predict_proba(input_data)[0][1]  # Probability of class 1
    prediction = model.predict(input_data)[0]
    risk = get_risk_level(prob)

    st.success(f"Hello, **{name}**! Based on your inputs, your predicted **diabetes risk level** is:")
    st.markdown(f"<h2 style='text-align: center; color: #e74c3c;'>{risk}</h2>", unsafe_allow_html=True)

    st.markdown("---")

    with st.expander("⚠️ Model Accuracy Info"):
        st.info("""
        This prediction is based on a machine learning model trained on historical health data.
        While it achieves good accuracy (~78-79%), it is not a substitute for professional medical advice.
        Always consult a healthcare provider for clinical diagnosis.
        """)

# === Footer ===
st.markdown("<hr style='margin-top:50px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:12px;'>Built for educational purposes 🧠</p>",
            unsafe_allow_html=True)

#streamlit run app.py
