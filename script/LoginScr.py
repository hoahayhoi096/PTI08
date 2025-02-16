from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic 
import os
from model.database import AccountDatabase

class Login(QMainWindow):
    def __init__(self, controller):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Login.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        self.database = AccountDatabase()
        self.database.load_data()
        for account in self.database.account_list:
            print("Tài khoản: ", account.email, "-", account.password)





