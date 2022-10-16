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


# # TODO написать jnghfdre json post запросом на сервер
# def json_to_api(url):
#     pass
#
#
# # TODO написать получение json get запросом с сервера
# def json_from_api(url):
#     pass
#
#
# def json_to_pandas(data, nrows):
#     data = data['transactions']
#     result = pd.DataFrame.from_dict(data).T
#     result = result[:nrows]
#     result.index = result.index.astype(int)
#     result['amount'] = result['amount'].astype(int)
#     result['passport'] = result['passport'].astype(str)
#     result['date'] = pd.to_datetime(result['date'], format='%Y-%m-%dT%H:%M:%S')
#     result['account_valid_to'] = pd.to_datetime(result['account_valid_to'], format='%Y-%m-%d')
#     result['date_of_birth'] = pd.to_datetime(result['date_of_birth'], format='%Y-%m-%d')
#     result['passport_valid_to'] = pd.to_datetime(result['passport_valid_to'], format='%Y-%m-%d')
#     return result
#
#
# def load_data(file, nrows=100000):
#     if nrows <= 0:
#         return pd.DataFrame()
#     with open(file) as json_file:
#         data = json.load(json_file)
#     return json_to_pandas(data, nrows)

def load_data(file, nrows=10000):
    if nrows <= 0:
        return pd.DataFrame()
    data = file
    data = data['pattern_1']
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


def visualisation(file):
    st.header("Транзакции")
    df = load_data(file)
    st.dataframe(df)


if __name__ == '__main__':
    if 'welcomed' not in st.session_state:
        st.balloons()
        st.session_state['welcomed'] = 'welcomed'
    f = open("transactions.json", "r")
    visualisation(f.read())
