import pandas as pd
import streamlit as st



def load_data(path):


    with st.form("Voir les données du formulaire"):
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
    st.write("Outside the form")
    return df