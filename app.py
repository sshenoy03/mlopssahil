import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('/random_forest_model.joblib')

# Title and description
st.title("Customer Churn Prediction")
st.write("Enter customer details to predict churn:")

# User inputs for features (customize based on model requirements)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
account_balance = st.number_input("Account Balance", min_value=0, value=10000)
years_with_company = st.slider("Years with Company", 0, 20, 5)
number_of_products = st.slider("Number of Products", 1, 5, 1)
is_active_member = st.selectbox("Is Active Member?", ["Yes", "No"])

# Convert input data to the required format for prediction
input_data = np.array([[age, account_balance, years_with_company, number_of_products, 1 if is_active_member == "Yes" else 0]])

# Predict churn
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write("The customer is likely to churn.")
    else:
        st.write("The customer is not likely to churn.")
