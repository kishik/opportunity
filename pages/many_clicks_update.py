import requests
import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    delay = st.number_input('Insert minutes of delay', value=5, min_value=1, step=1)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        requests.get(url='127.0.0.1:5000/set_many_click_delay/{0}'.format(delay))
        st.write("delay", delay)
