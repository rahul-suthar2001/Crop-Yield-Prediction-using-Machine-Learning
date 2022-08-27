
import pickle
import numpy as np 
import streamlit as st
filename = "crop_model.pkl"
model = pickle.load(open(filename, 'rb'))

st.header("Crop Predication")
st.write("Predicting the crop  based of given details")

Rainfall = st.text_input("Enter the rainfall")
Temperature = st.text_input("Enter the temperature")
ph= st.text_input("Enter the pH")

if st.button('Find'):
    query = np.array([[Rainfall, Temperature, ph]])
    result = model.predict(query)[0]
    if result:
        result = "Crop you should produce is "+str(result)
        st.header(result)
    else:
        st.header("Error")