
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Load your model file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('How Age regulates Billing charges and how much patients spend for a particular medical condition predictor App')

# Add input widgets for user inputs
age = st.slider( min_value=18, max_value=85, value=51)

medical_condition = st.selectbox(
    " Medical Condition",
    ["Cancer", "Diabetes", "Asthma", "Obesity", "Arthritis", "Hypertension" ]
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
