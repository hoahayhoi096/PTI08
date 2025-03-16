from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6 import uic 
from PyQt6.QtCore import Qt
import os
from config import Config
from script.DialogScr import AddDialog, EditDialog

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

        self.pushButtonAdd.clicked.connect(self.onPushButtonAdd)
        self.pushButtonEdit.clicked.connect(self.onPushButtonEdit)


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
    
    def onPushButtonAdd(self):
        # Lấy dòng hiện tại đang chọn trong listWidgetAnime
        current_row = self.listWidgetAnime.currentRow()

        add_dialog = AddDialog()

        # Hiển thị dialog và kiểm tra nếu người dùng nhấn OK thì thêm vào ds anime
        if add_dialog.exec():
            # Lấy dữ liệu từ hộp thoại ở dụng json (dictionary)
            inputs = add_dialog.return_input_fields()

            # Thêm bộ anime mới vào listWidgetAnime 
            self.listWidgetAnime.insertItem(current_row, inputs["title"])

            # Lưu dữ liệu vào cơ sơ dữ liệu
            self.database.add_item_from_dict(inputs)


    def onPushButtonEdit(self):
        # Lấy dòng hiện tại đang chọn trong listWidgetAnime
        current_row = self.listWidgetAnime.currentItem()

        if current_row:
            # Lấy id của anime cần sửa
            edit_id = current_row.data(Qt.ItemDataRole.UserRole)

            edit_item = self.database.get_item_by_id(edit_id)

            edit_dialog = EditDialog(edit_item)
            # Mở dialog và kiểm tra nếu người dùng nhấn OK thì sửa thông tin anime
            if edit_dialog.exec():
                inputs = edit_dialog.return_input_fields()
                # Đặt ngay cho tiêu đồ của dòng đang chọn thành tiêu đề mới luôn 
                current_row.setText(inputs["title"])
                # Sửa thông tin anime trong cơ sở dữ liệu
                self.database.edit_item_from_dict(edit_id, inputs)


        
