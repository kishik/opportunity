from st_aggrid import AgGrid
from visualisation import load_data, page_config

page_config()

AgGrid(load_data('../transactions.json', 10))
