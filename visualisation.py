import json

import pandas as pd
import streamlit as st

api_url = 'http://api.openweathermap.org/geo/1.0/direct'


def page_config():
    st.set_page_config(
        page_title="Transactions",
        page_icon=":shark:",
        layout="wide",
        initial_sidebar_state="expanded",

    )


def load_data(data, nrows=0):
    if nrows <= 0:
        return pd.DataFrame()
    data = data['transactions']
    result = pd.DataFrame.from_dict(data).T
    result = result[:nrows]
    result.index = result.index.astype(int)
    result['amount'] = result['amount'].astype(int)
    result['passport'] = result['passport'].astype(str)
    result['date'] = pd.to_datetime(result['date'], format='%Y-%m-%dT%H:%M:%S')
    result['account_valid_to'] = pd.to_datetime(result['account_valid_to'], format='%Y-%m-%d')
    result['date_of_birth'] = pd.to_datetime(result['date_of_birth'], format='%Y-%m-%d')
    result['passport_valid_to'] = pd.to_datetime(result['passport_valid_to'], format='%Y-%m-%d')
    return result


def load_patterns(data):
    data = data['fraud_transactions']
    result = pd.DataFrame.from_dict(data).T

    result.index = result.index.astype(str)
    return result



def visualisation(file, nrows=10000):
    st.header("Транзакции")
    df = load_data(json.loads(file), nrows)
    st.dataframe(df)


if __name__ == '__main__':
    if 'welcomed' not in st.session_state:
        st.balloons()
        st.session_state['welcomed'] = 'welcomed'
    f = open("transactions.json", "r")
    visualisation(f.read())
