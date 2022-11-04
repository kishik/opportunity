import requests
import streamlit as st

# from visualisation import load_pat
from visualisation import load_data

test = "3649244372,3649244373,3649244374,3649244375,3649244376,3649244377"

url = 'http://127.0.0.1:5000/get_transactions'

if __name__ == '__main__':
    # df = load_patterns(st.session_state['paterns'].json())
    patern = requests.get(url)
    df = load_data(patern.json(), 1000)
    st.dataframe(df)
