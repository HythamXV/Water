import streamlit as st
import pandas as pd
import pickle
import os

print(f"Current Working Directory: {os.getcwd()}")
print(f"Directory Contents: {os.listdir()}")

# Update the model path to the correct absolute path
model_path = "RandomForestClassifier_model2.sav"

def load_model():
    try:
        if os.path.exists(model_path):
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
            print("Model loaded successfully!")
            return model
        else:
            print(f"Model file not found at: {model_path}")
            return None
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

def main():
    st.title("Water quality prediction Web App")
    st.info('Easy Application For Water quality prediction Diseases')
    
    # Moved the model loading inside the load_model function
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
    prediction = model.predict(df)
    if prediction[0] == 0:
        st.write('The water is not potable.')
    else:
        st.write('The water is potable.')

if __name__ == "__main__":
    main()
