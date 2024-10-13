
import pickle
import joblib
import streamlit as st
import numpy as np
import pandas as pd

# Load your model file
with open('model (2).pkl', 'rb') as f:
    model = pickle.load(f)

st.title('How Age regulates Billing charges and how much patients spend for a particular medical condition predictor App')

# Add input widgets for user inputs
age = st.slider("Age", min_value=18, max_value=85, value=51)

medical_condition = st.selectbox(
    " Medical Condition",
    ["Cancer", "Diabetes", "Asthma", "Obesity", "Arthritis", "Hypertension" ]
)

insurance_provider = st.selectbox(
    "Insurance Provider",
    ['Blue Cross', 'Medicare', 'Aetna', 'UnitedHealthcare', 'Cigna']
)

medication = st.selectbox(
    "Medication",
    ["Paracetamol", "Ibuprofen", "Aspirin", "Penicillin", "Lipitor"]
)

# When the 'Predict' button is clicked
if st.button("Predict"):
    # Prepare the input data as a DataFrame (since pipelines often expect a DataFrame)
    input_data = pd.DataFrame({
        'Age': [age],
        ' Medical Condition': [medical_condition],
        'Insurance Provider': [insurance_provider],
        'Medication': [medication]
    })
    prediction = model.predict(input_data)[0].round(2)
    st.write(f'The predicted value is: {prediction} thousand dollars')
