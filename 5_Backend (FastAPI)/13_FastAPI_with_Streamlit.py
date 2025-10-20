# using the FastAPI endpoint in Streamlit code, to display the result in browser
# Need to install streamlit, `pip install streamlit`

import streamlit as st
import requests

st.title("Customer insurance category prediction")
st.markdown("Enter the input details below:")

API_URL = "http://127.0.0.1:8000/predict"

age = st.number_input("Age", min_value=1, max_value=150, value=30)
weight = st.number_input("Weight (kg)", min_value=0, value=50)
height = st.number_input("Height (meters)", min_value=0.0, max_value=2.5, value=1.2)
income_lpa = st.number_input("Income LPA", min_value=0, value=6)
smoker = st.selectbox("Somker?", options=[True, False])
city = st.text_input('Current residence city', value='Vijayawada')
occupation = st.selectbox('occupation', options=['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium category"):
    input_data = {
        'age':age,
        'weight':weight,
        'height':height,
        'income_lpa':income_lpa,
        'smoker':smoker,
        'city':city,
        'Occupation':occupation
    }

    try:
        response = requests.post(API_URL, json = input_data)
        if response.status_code == 200:
            result = response.json()
            print(result)
            st.success(f"Predicted Insurance premium category: **{result['Predicted-category']}**")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FAstAPI server")