from model.account import Account
from data.data_io import load_account_json_data, write_account_json_data

class AccountDatabase:
    def __init__(self):
        self.account_list = list()
        self.account_dict_data = load_account_json_data()

    # Lấy dữ liệu json chuyển thành danh sách đối tượng Account
    def load_data(self):
        for account_dict in self.account_dict_data:
            account = Account(email = account_dict["email"],
                              password = account_dict["password"])
            self.account_list.append(account)

    