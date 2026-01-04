import streamlit as st
import pandas as pd
import pickle


with open("health_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Health Risk Prediction App")

age = st.number_input("Enter Age", min_value=0, max_value=120)
bp = st.number_input("Enter Blood Pressure")
chol = st.number_input("Enter Cholesterol")

if st.button("Predict"):
    input_df = pd.DataFrame([[age, bp, chol]], columns=["age","bp","chol"])
    prediction = model.predict(input_df)
    
    if prediction[0]==0:
        st.success("Low Risk")
    elif prediction[0]==1:
        st.warning("Moderate Risk")
    else:
        st.error("High Risk")
