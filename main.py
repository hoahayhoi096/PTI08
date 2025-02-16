from PyQt6.QtWidgets import QApplication, QWidget
import sys
from appController import Controller


if __name__ == '__main__':
    app = QApplication(sys.argv)

    controller = Controller()
    controller.show_login_page()
    
    app.exec()
