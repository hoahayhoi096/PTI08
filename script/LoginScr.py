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

        self.pushButtonDangNhap.clicked.connect(self.onPushButtonDangNhap)
    
    def onPushButtonDangNhap(self):
        # Kiểm tra tài khoản và mật khẩu người dùng nhập vào có tồn tại trong database không
        taiKhoan = self.lineEditTaiKhoan.text()
        matKhau = self.lineEditMatKhau.text()
        
        isAuth = False
        for account in self.database.account_list:
            if account.email == taiKhoan and account.password == matKhau:
                isAuth = True
                break
        if isAuth == True:
            self.controller.show_main_page()
            self.close()
        else:
            QMessageBox.information(self, "Đây là thông báo!", "Đăng nhập thất bại, tài khoản hoặc mật khẩu không chính xác!")


        





