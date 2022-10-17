import requests
import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    years_from = st.number_input('Insert from years', value=50, min_value=0, step=1)
    years_to = number = st.number_input('Insert to years', value=55, min_value=0, step=1)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # send get req
        requests.get(url='127.0.0.1:5000/set_bad_age/{0}/{1}'.format(years_from, years_to))
        st.write("years_from", years_from, "years_to", years_to)
