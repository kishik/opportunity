import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    hour_from = st.number_input('Insert from hour', value=14, min_value=0, max_value=23, step=1)
    hour_to = number = st.number_input('Insert to hour', value=16, min_value=0, max_value=23, step=1)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # send get req
        st.write("hour_from", hour_from, "hour_to", hour_to)
