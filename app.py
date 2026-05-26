import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
# Ensure 'model.pkl' is in the same directory as 'app.py'
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Dynamic Pricing Engine')
st.write('Enter the following details to get a predicted optimal price:')

# Input fields for prediction
demand = st.slider('Demand', min_value=1, max_value=200, value=100)
competitor_price = st.slider('Competitor Price', min_value=1.0, max_value=300.0, value=150.0, step=0.5)
day = st.slider('Day of Month', min_value=1, max_value=31, value=15)
month = st.slider('Month', min_value=1, max_value=12, value=6)

# Predict button
if st.button('Predict Price'):
    # Prepare input data as a DataFrame, matching the training features
    input_data = pd.DataFrame([[demand, competitor_price, day, month]],
                                columns=['demand', 'competitor_price', 'day', 'month'])
    
    # Make prediction
    predicted_price = model.predict(input_data)[0]
    
    st.success(f'The predicted optimal price is: ${predicted_price:.2f}')
