import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle
import os
from try_1 import load_model

def main():
    st.title("Water quality prediction Web App")
    st.info('Easy Application For Water quality prediction Diseases')

    # Load the model using the external loader
    model = load_model()

    st.sidebar.write("")
    st.sidebar.header("Feature Selection")

    ph = st.text_input("ph")
    Hardness = st.text_input("Hardness")
    Solids = st.text_input("Solids")
    Chloramines = st.text_input("Chloramines")
    Sulfate = st.text_input("Sulfate")
    Conductivity = st.text_input("Conductivity")
    Organic_carbon = st.text_input("Organic_carbon")
    Trihalomethanes = st.text_input("Trihalomethanes")
    Turbidity = st.text_input("Turbidity")

    data = {
        'ph': [ph],
        'Hardness': [Hardness],
        'Solids': [Solids],
        'Chloramines': [Chloramines],
        'Sulfate': [Sulfate],
        'Conductivity': [Conductivity],
        'Organic_carbon': [Organic_carbon],
        'Trihalomethanes': [Trihalomethanes],
        'Turbidity': [Turbidity]
    }
    df = pd.DataFrame(data)

    # Create a button to execute the prediction
    if st.button('Predict Potability'):
        if model is not None:
            prediction = model.predict(df)
            if prediction[0] == 0:
                st.write('The water is not potable.')
            else:
                st.write('The water is potable.')
        else:
            st.write('Error: Model not loaded.')

if __name__ == "__main__":
    main()
