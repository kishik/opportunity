from st_aggrid import AgGrid

from visualisation import load_data

AgGrid(load_data('../transactions.json', 10))
