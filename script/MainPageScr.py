from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QListView, QAbstractItemView
from PyQt6 import uic 
from PyQt6.QtCore import Qt, QSize
import os
from config import Config
from script.DialogScr import AddDialog, EditDialog
from script.AnimeItemScr import AnimeItemWidget

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
        self.pushButtonDelete.clicked.connect(self.onPushButtonDelete)

        self.setup_rank_page()

        self.pushButtonTopAnime.clicked.connect(self.onPushButtonTopAnime)


    def onPushButtonAccount(self):
        self.stackedWidget.setCurrentIndex(0)

    def onPushButtonHome(self):
        self.stackedWidget.setCurrentIndex(1)

    def onPushButtonAnime(self):
        self.stackedWidget.setCurrentIndex(2)

    def onPushButtonManager(self):
        self.stackedWidget.setCurrentIndex(3)

    def setup_manager_page(self):
        # Xoá đi dữ liệu rác có từ trước nếu có
        self.listWidgetAnime.clear()
        # Tải toàn bộ dữ liệu json vào ds đối tượng Anime 
        self.database.load_data()


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

    def onPushButtonDelete(self):
        # Lấy chỉ số của item hiện tại trong listWidget
        curr_index = self.listWidgetAnime.currentRow()

        if curr_index == -1:
            QMessageBox.warning(self, "Error", "Bạn chưa chọn anime để xoá!")
            return
        
        # Lấp anime hiện tại đang được chọn
        item = self.listWidgetAnime.item(curr_index)
        item_title = item.text()

        # Lấy id của bộ anime vừa chọn thông qua User role 
        anime_id = item.data(Qt.ItemDataRole.UserRole)

        # Hiển thị hộp thoại xác nhận 
        question = QMessageBox.question(
            self,
            "Remove Anime",
            f"Bạn có muốn xoá bộ anime '{item_title}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if question == QMessageBox.StandardButton.Yes:
            # Xoá item khỏi listWidget
            self.listWidgetAnime.takeItem(curr_index)

            # Gọi hàm xoá anime khỏi database(.json)
            self.database.delete_item(anime_id)

            QMessageBox.information(self, "Success", "Bạn đã xoá anime: " + item_title)

    def setup_rank_page(self):
        # Xoá hết dữ liệu cũ/rác trong listwidget 
        # Đặt khoảng cách giữa các widget con trong listWidget 
        self.listWidgetAnimeRanking.clear()
        self.listWidgetAnimeRanking.setSpacing(10)

        # Đặt chế độ hiển thị item theo chiều ngang 
        self.listWidgetAnimeRanking.setFlow(QListView.Flow.LeftToRight)

        # Bật thanh cuộng ngang (chỉ cần áp dụng)
        self.listWidgetAnimeRanking.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listWidgetAnimeRanking.setWrapping(False)  # Không cho phép wrap item xuống dòng

        # Load các widget chứa thông tin các bộ anime lên listWidget

        # Lấy danh sách các đối tượng anime 
        anime_list = self.database.anime_list

        for anime in anime_list:
            animeWidget = AnimeItemWidget(anime)

            # Tạo đối tượng con của listWidgetAnimeRanking
            item = QListWidgetItem(self.listWidgetAnimeRanking)

            # Lưu lại id của bộ anime
            item.setData(Qt.ItemDataRole.UserRole, anime.id)
            # Đặt kích thước cố định cho animeWidget
            animeWidget.setFixedSize(250, 500)
            # Đặt kích thước cho phần tử con của listWidgetAnimeRanking
            item.setSizeHint(QSize(250, 500))

            self.listWidgetAnimeRanking.addItem(item)
            # Kết hợp item và animeWidget để hiển thị đúng nội dung mong muốn trong listWidgetAnimeRanking
            self.listWidgetAnimeRanking.setItemWidget(item, animeWidget)

    def onPushButtonTopAnime(self):
        self.database.sort_item_by_rating()
        self.setup_rank_page()

        




    


        


        
