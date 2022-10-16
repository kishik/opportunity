import sqlite3

PATH_TO_DB = 'backend/db/database.db'


class SQLlib:
    def __init__(self) -> None:
        self.con = sqlite3.connect(PATH_TO_DB, check_same_thread=False)
        self.cur = self.con.cursor()

    def add_transaction(self, transaction_id: str, t_data: dict) -> None:
        self.cur.execute("INSERT OR REPLACE INTO transactions (id, date, card, account, account_valid_to, client,"
                         "last_name, first_name, patronymic, date_of_birth, passport, passport_valid_to, "
                         "phone, oper_type, amount, oper_result, terminal, terminal_type, city, address)"
                         "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (transaction_id, t_data['date'], t_data['card'], t_data['account'],
                          t_data['account_valid_to'], t_data['client'], t_data['last_name'],
                          t_data['first_name'], t_data['patronymic'], t_data['date_of_birth'],
                          str(t_data['passport']), t_data['passport_valid_to'], t_data['phone'],
                          t_data['oper_type'], t_data['amount'], t_data['oper_result'],
                          t_data['terminal'], t_data['terminal_type'], t_data['city'], t_data['address']))
        self.con.commit()

    def get_transactions(self) -> list:
        return self.cur.execute("SELECT * FROM transactions").fetchall()

