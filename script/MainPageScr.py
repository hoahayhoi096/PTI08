from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic 
import os
from config import Config


class MainPage(QMainWindow):  
    def __init__(self, controller):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/MainPage.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller

        self.pushButtonAccount.clicked.connect(self.onPushButtonAccount)
        self.pushButtonHome.clicked.connect(self.onPushButtonHome)
        self.pushButtonAnime.clicked.connect(self.onPushButtonAnime)
        self.pushButtonManager.clicked.connect(self.onPushButtonManager)

    def onPushButtonAccount(self):
        self.stackedWidget.setCurrentIndex(0)

    def onPushButtonHome(self):
        self.stackedWidget.setCurrentIndex(1)

    def onPushButtonAnime(self):
        self.stackedWidget.setCurrentIndex(2)

    def onPushButtonManager(self):
        self.stackedWidget.setCurrentIndex(3)


