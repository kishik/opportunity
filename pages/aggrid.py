from st_aggrid import AgGrid

from visualisation import load_data

if __name__ == '__main__':
    f = open("transactions.json", "r")
    AgGrid(load_data(f.read(), 10))
