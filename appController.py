from PyQt6.QtWidgets import QApplication, QWidget
import sys
from script.LoginScr import Login


class Controller: 
    def __init__(self):

        # Khởi tạo các cửa sổ 
        self.login_window = Login(self)

    def show_login_page(self):
        self.login_window.show()
