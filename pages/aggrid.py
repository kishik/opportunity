from st_aggrid import AgGrid

from visualisation import load_data

f = open("transactions.json", "r")
AgGrid(load_data(f.read(), 10))
