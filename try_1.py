import streamlit as st
import pandas as pd
import pickle
import os

print(f"Current Working Directory: {os.getcwd()}")
print(f"Directory Contents: {os.listdir()}")

# Update the model path to the correct absolute path
model_path = "RandomForestClassifier_model2.sav"

# Load the model
try:
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully!")
    else:
        print(f"Model file not found at: {model_path}")
        model = None
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None

def main():
    st.title("Water quality prediction Web App")
    st.info('Easy Application For Water quality prediction Diseases')
    
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
    df = pd.D
