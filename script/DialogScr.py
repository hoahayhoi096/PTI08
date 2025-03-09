import os

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.QtCore import QDate, QDir

from config import Config
try:
    from ui.add_dialog_ui import Ui_AddDialog
    from ui.edit_dialog_ui import Ui_EditDialog
except ImportError:
    pass

from model.anime import Anime
from model.database import date_to_text, format_date


class Dialog(QDialog):
    """
    Prorotype Dialog
    """
    def __init__(self, dialog_type):
        super().__init__()
        self.ui = None

        self.dir = QDir(Config.LOCAL_DIR)

    def _browse_files(self):
        fname = QFileDialog.getOpenFileName(self, 
                                            'Open file',
                                              './ui/images',
                                                )
        self.ui.uploadImageButton.setText(fname[0])
        return fname
    
    def return_input_fields(self) -> dict:
        # Lấy ngày tháng năm của người dùng nhập từ dateEdit
        date_input = self.ui.releasedateInput.date().toPyDate() # Format: yyyy-mm-dd

        # Lấy đường dẫn từ nut upload hình 
        image_path_input = self.ui.uploadImageButton.text()

        # Lấy link url từ người dùng nhập nếu không nhập thì gán bằng "None"
        if self.ui.urlInput.text() == "":
            url_input = "None"
        else:
            url_input = self.ui.urlInput.text()

        # Trả về json (dictionary) của dữ liệu người dùng nhập
        return {
            "title": self.ui.titleInput.text(),

            "release_date": date_to_text(date_input), 

            "image": self.dir.relativeFilePath(image_path_input),

            "rating": float(self.ui.ratingInput.text()),

            "link": url_input
        }
    
class AddDialog(Dialog):
    UI_LOCATION = os.path.join(Config.UI_DIR, "add_dialog.ui")
    def __init__(self):
        super().__init__(AddDialog)

        self.ui = uic.loadUi(self.UI_LOCATION, self)

        self.ui.uploadImageButton.clicked.connect(lambda: self._browse_files)

        self.ui.releasedateInput.setDisplayFormat("dd/MM/yyyy")
    
class EditDialog(Dialog):
    UI_LOCATION = os.path.join(Config.UI_DIR, "edit_dialog.ui")

    def __init__(self):
        super().__init__(EditDialog)

        self.ui = uic.loadUi(self.UI_LOCATION, self)