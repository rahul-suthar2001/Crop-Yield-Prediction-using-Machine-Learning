import production as pt
import pickle
import numpy as np 
import streamlit as st

filename = "production_model.pkl"
model = pickle.load(open(filename, 'rb'))

st.header("Crop Production")
st.write("Predicting the crop production based of given details")


year = np.arange(1990,2050)
state_name = st.selectbox("Select state name",pt.state_list)
district_name = st.selectbox("Select district name",pt.District_list)
crop_name = st.selectbox("Select crop name",pt.crop_list)
crop_year =  st.selectbox("select crop year",year)
Season = st.selectbox("Select Season of crop",pt.season_list)
Area =  st.text_input("Enter the area of land")
zones = pt.get_zonal_names(state_name)



if st.button('Find'):

    query = pt.encoded_data(state_name, district_name, Season, zones, crop_name, crop_year, Area)
    result = model.predict(query)[0]
    if result:
        result = "Production => "+str(result)
        if int(Area)==0:
            st.header(0)
        else:
            st.header(result)
    else:
        st.header("Error")
