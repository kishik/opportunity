import requests
import streamlit as st

from main_page import get_ids
from main_page import load_data

url = 'http://127.0.0.1:5000/get_transactions_by_ids/' + get_ids('pattern_3')
patern = requests.get(url)
st.header("Подозрительная активность в ночное время")
df = load_data(patern.json(), 10000)
st.dataframe(df)

with st.form("my_form"):
    st.write("Inside the form")
    hour_from = st.number_input('Insert from hour', value=0, min_value=0, max_value=23, step=1)
    hour_to = number = st.number_input('Insert to hour', value=5, min_value=0, max_value=23, step=1)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        requests.get(url='http://127.0.0.1:5000/set_night_time/{0}/{1}'.format(hour_from, hour_to))
        st.write("hour_from", hour_from, "hour_to", hour_to)
