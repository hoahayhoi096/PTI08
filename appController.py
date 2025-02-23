from PyQt6.QtWidgets import QApplication, QWidget
import sys
from script.LoginScr import Login
from script.MainPageScr import MainPage

class Controller: 
    def __init__(self):

        # Khởi tạo các cửa sổ 
        self.login_window = Login(self)
        self.main_window = MainPage(self)

    def show_login_page(self):
        self.login_window.show()

    def show_main_page(self):
        self.main_window.show()
