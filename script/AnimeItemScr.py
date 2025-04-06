from PyQt6.QtWidgets import QWidget
from config import Config
import os
from PyQt6 import uic
from model.anime import Anime
from PyQt6.QtGui import QPixmap


class AnimeItemWidget(QWidget):
    UI_LOCATION = os.path.join(Config.UI_DIR, "anime_column.ui")

    def __init__(self, anime: Anime):
        QWidget.__init__(self)
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        self.anime = anime

        self.display_description()

    # Hàm hiển thị thông tin của Anime
    def display_description(self):
        self.ui.animeTitle.setText(self.anime.title)
        img_pixmap = QPixmap(self.anime.image)
        self.ui.animeView.setPixmap(img_pixmap)

        descriptiong_text = self.anime.release_date + "\n" \
                            + "Rating: " + str(self.anime.rating) + "/10"
        self.ui.animeInfo.setText(descriptiong_text)