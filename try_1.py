import streamlit as st
import pandas as pd
import numpy as np
import plotly .express as px
import pickle
import os
from model_loader import load_model
from RandomForestClassifier_model2_loader import load_model

def main():
    st.title("Water quality prediction Web App")
    st.info('Easy Application For Water quality prediction Diseases')
# model_loader.py

def load_model():
    model_path = "RandomForestClassifier_model2.sav"
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

print(f"Current Working Directory: {os.getcwd()}")
print(f"Directory Contents: {os.listdir()}")

#df=pd.read_csv("water.csv")

st.sidebar.write ("")
#st.sidebar.markdown ("hhhh")import pickle

st.sidebar.header("Feature Selection")


ph=st.text_input("ph")
Hardness=st.text_input("Hardness")
Solids=st.text_input("Solids")
Chloramines=st.text_input("Chloramines")
Sulfate=st.text_input("Sulfate")
Conductivity=st.text_input("Conductivity")
Organic_carbon=st.text_input("Organic_carbon")
Trihalomethanes=st.text_input("Trihalomethanes")
Turbidity=st.text_input("Turbidity")
Potability=st.text_input("Potability")


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

# إنشاء زر لتنفيذ التنبؤ
if st.button('Predict Potability'):
    prediction = model.predict(df)
    if prediction[0] == 0:
        st.write('The water is not potable.')
    else:
        st.write('The water is potable.')

if __name__ == "__main__":
    main()





