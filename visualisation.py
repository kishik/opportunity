import json
import streamlit as st
import pandas as pd


# @st.cache
def load_data(file, nrows=None):
    if nrows <= 0:
        return pd.DataFrame()
    with open('transactions.json') as json_file:
        data = json.load(json_file)
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


def visualisation(file, nrows=10000):
    st.header("Транзакции")
    df = load_data(file, nrows)
    st.dataframe(df)


if __name__ == '__main__':
    st.set_page_config(
        page_title="Transactions",
        page_icon=":shark:",
        layout="wide",
        initial_sidebar_state="expanded",

    )
    if 'welcomed' not in st.session_state:
        st.balloons()
        st.session_state['welcomed'] = 'welcomed'
    visualisation('transactions.json')
