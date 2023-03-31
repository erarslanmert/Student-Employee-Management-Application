# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\erars\PycharmProjects\disdem\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QMessageBox
import main_page, new_user

user_active = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(307, 525)
        MainWindow.setStyleSheet("background-color: rgb(0, 41, 61);\n"
                             "selection-background-color: rgb(255, 255, 255);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        MainWindow.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(MainWindow, clicked = lambda : self.user_loggedin())
        self.pushButton.setGeometry(QtCore.QRect(44, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow, clicked = lambda : MainWindow.close())
        self.pushButton_2.setGeometry(QtCore.QRect(160, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(42, 170, 221, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 280, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(40, 122, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("color:  rgb(255, 230, 207);\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setStyleSheet("color:  rgb(255, 230, 207);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(MainWindow)
        self.checkBox.setGeometry(QtCore.QRect(110, 350, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color:  rgb(255, 230, 207);")
        self.checkBox.setObjectName("checkBox")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(40, 460, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet("color: rgb(254, 255, 231);\n"
                               "")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(105, 20, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("logo_hq.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")


        self.label_3.mousePressEvent = self.handle_mouse_press


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.setText('erarslan.mert')
        self.lineEdit_2.setText('mert1993')

    def handle_mouse_press(self, event):
        new_user.open_newuser_reg()

    def user_loggedin(self):
        user_active = True
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if user_name == 'erarslan.mert' and  password == 'mert1993':
            self.lineEdit.setDisabled(True)
            self.lineEdit_2.setDisabled(True)
            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.checkBox.setDisabled(True)
            main_page.open_mainpage()

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Kullanici adi veya parola hatali, eger parolaniz buyuk/kucuk harf, ozel karakter veya"
                            " sayi iceriyorsa bu karakterlere dikkat ederek tekrar deneyiniz!")
            msg_box.setWindowTitle("Hatali Giris")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giris Sayfasi"))
        self.pushButton.setToolTip(_translate("MainWindow", "Giris Yap"))
        self.pushButton.setText(_translate("MainWindow", "Giris Yap"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Iptal"))
        self.pushButton_2.setText(_translate("MainWindow", "Iptal"))
        self.label.setToolTip(_translate("MainWindow", "Kullanici Numarasi"))
        self.label.setText(_translate("MainWindow", "Kullanici Ismi"))
        self.label_2.setToolTip(_translate("MainWindow", "Sifre"))
        self.label_2.setText(_translate("MainWindow", "Sifre"))
        self.checkBox.setText(_translate("MainWindow", "Beni Hatirla"))
        self.label_3.setToolTip(_translate("MainWindow", "Kullanici Numarasi"))
        self.label_3.setText(_translate("MainWindow", "Yeni Kullanici Kaydi"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("WindowsVista"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())