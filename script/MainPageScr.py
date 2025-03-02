from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6 import uic 
from PyQt6.QtCore import Qt
import os
from config import Config


class MainPage(QMainWindow):  
    def __init__(self, controller):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/MainPage.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        self.database = controller.database

        self.pushButtonAccount.clicked.connect(self.onPushButtonAccount)
        self.pushButtonHome.clicked.connect(self.onPushButtonHome)
        self.pushButtonAnime.clicked.connect(self.onPushButtonAnime)
        self.pushButtonManager.clicked.connect(self.onPushButtonManager)

        self.setup_manager_page()



    def onPushButtonAccount(self):
        self.stackedWidget.setCurrentIndex(0)

    def onPushButtonHome(self):
        self.stackedWidget.setCurrentIndex(1)

    def onPushButtonAnime(self):
        self.stackedWidget.setCurrentIndex(2)

    def onPushButtonManager(self):
        self.stackedWidget.setCurrentIndex(3)

    def setup_manager_page(self):
        # Tải toàn bộ dữ liệu json vào ds đối tượng Anime 
        self.database.load_data()

        # Xoá đi dữ liệu rác có từ trước nếu có
        self.listWidgetAnime.clear()

        # Thêm dữ liệ vào listWidget
        for item in self.database.anime_list:
            # Tạo phần tử con của listWidget
            listWidgetItem = QListWidgetItem(item.title)
            # Lưu lại id của anime vào UserRole
            listWidgetItem.setData(Qt.ItemDataRole.UserRole, item.id)

            # Thêm phần phần tử con vào listWidget
            self.listWidgetAnime.addItem(listWidgetItem)

        self.listWidgetAnime.setCurrentRow(0)


