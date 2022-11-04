import requests
import streamlit as st

from main_page import get_ids
from main_page import load_data

url = 'http://127.0.0.1:5000/get_transactions_by_ids/' + get_ids('pattern_1')
patern = requests.get(url)
st.header("Множество кликов за короткий промежуток времени")
df = load_data(patern.json(), 10000)
st.dataframe(df)

with st.form("my_form"):
    st.write("Inside the form")
    delay = st.number_input('Insert minutes of delay', value=5, min_value=1, step=1)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        requests.get(url='http://127.0.0.1:5000/set_many_click_delay/{0}'.format(delay))
        st.write("delay", delay)
