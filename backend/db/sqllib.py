import sqlite3

con = sqlite3.connect('db/database.db', check_same_thread=False)
cur = con.cursor()