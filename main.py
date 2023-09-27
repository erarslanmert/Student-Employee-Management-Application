# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\erars\PycharmProjects\disdem\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QMessageBox
import data_objects
import database_corrector
import date_consistency
import main_page, new_user
import connect_database
import trial


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "selection-background-color: rgb(0, 170, 127);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 280, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "selection-background-color: rgb(0, 170, 127);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
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
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label.setFont(font)
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

        self.lineEdit.textChanged.connect(self.lineedit_activity)
        self.lineEdit_2.textChanged.connect(self.lineedit_activity)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        connect_database.download_files('user_list.txt')
        connect_database.download_files('student_data.txt')
        connect_database.download_files('employee_data.txt')
        connect_database.download_files('temporary_student.txt')

        database_corrector.check_table_versus_file()
        database_corrector.check_lesson_empty()
        connect_database.upload_files('employee_data.txt')
        connect_database.upload_files('student_data.txt')

        with open('student_data.txt', 'r', encoding="utf-8") as f:
            data_objects.students = json.load(f)
        with open('employee_data.txt', 'r', encoding="utf-8") as f:
            data_objects.employees = json.load(f)
        with open('temporary_student.txt', 'r', encoding="utf-8") as f:
            data_objects.temporary_students = json.load(f)

        date_consistency.convert_dates_in_list(data_objects.students)
        date_consistency.convert_dates_in_list(data_objects.employees)

        with open("student_data.txt", "w", encoding="utf-8") as f:
            f.writelines(json.dumps(data_objects.students, default=str))
        with open("employee_data.txt", "w", encoding="utf-8") as f:
            f.writelines(json.dumps(data_objects.employees, default=str))


        def process_student_data_file():
            with open('student_data.txt', 'r', encoding="utf-8") as f:
                data_objects.students = json.load(f)

            # Process the data
            for item in data_objects.students:
                name = item.get('name')
                if name and ' ' in name:
                    item['name'] = name.replace(' ', '-')
                if name.endswith('-'):
                    item['name'] = name.replace('-', '')   # Remove the trailing '-' if it is not followed by a word character

                for key, value in item.items():
                    if isinstance(value, str) and value.endswith('\n') or ('\n') in value:
                        item[key] = value.replace('\n','')
            for item in data_objects.students:
                name = item.get('surname')
                if name and ' ' in name:
                    item['surname'] = name.replace(' ', '-')
                if name.endswith('-'):
                    item['surname'] = name.replace('-', '')   # Remove the trailing '-' if it is not followed by a word character

                for key, value in item.items():
                    if isinstance(value, str) and value.endswith('\n') or ('\n') in value:
                        item[key] = value.replace('\n','')



            # Save the updated data back to the file
            with open("student_data.txt", "w", encoding="utf-8") as f:
                f.writelines(json.dumps(data_objects.students, default=str))

        process_student_data_file()
        
        def process_employee_data_file():
            with open('employee_data.txt', 'r', encoding="utf-8") as f:
                data_objects.employees = json.load(f)

            # Process the data
            for item in data_objects.employees:
                name = item.get('name')
                if name and ' ' in name:
                    item['name'] = name.replace(' ', '-')
                if name.endswith('-'):
                    item['name'] = name.replace('-', '')   # Remove the trailing '-' if it is not followed by a word character

            for item in data_objects.employees:
                name = item.get('surname')
                if name and ' ' in name:
                    item['surname'] = name.replace(' ', '-')
                if name.endswith('-'):
                    item['surname'] = name.replace('-', '')  # Remove the trailing '-' if it is not followed by a word character

                for key, value in item.items():
                    if isinstance(value, str) and value.endswith('\n') or ('\n') in value:
                        item[key] = value.replace('\n','')


            # Save the updated data back to the file
            with open("employee_data.txt", "w", encoding="utf-8") as f:
                f.writelines(json.dumps(data_objects.employees, default=str))

        process_employee_data_file()

        with open('user_list.txt', 'r', encoding="utf-8") as f:
            data_objects.users = json.load(f)
        with open('student_data.txt', 'r', encoding="utf-8") as f:
            data_objects.students = json.load(f)
        with open('employee_data.txt', 'r', encoding="utf-8") as f:
            data_objects.employees = json.load(f)
        with open('remember_me.txt', 'r', encoding="utf-8") as f:
            self.remember_user = json.load(f)


        if len(self.remember_user) == 1:
            self.checkBox.setChecked(True)
        else:
            pass

        if self.checkBox.isChecked() == True:
            self.lineEdit.setText(self.remember_user[0]['user_name'])
            self.lineEdit_2.setText(self.remember_user[0]['password'])
        else:
            pass

    def lineedit_activity(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(True)

    def handle_mouse_press(self, event):
        new_user.open_new_user()
        with open('user_list.txt', 'r', encoding="utf-8") as f:
            data_objects.users = json.load(f)


    def user_loggedin(self):
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        data_correct = False
        for user in data_objects.users:
            if user_name == user['user_name'] and password == user['password']:
                data_correct = True
                data_objects.user_logged_in = user
            else:
                pass
        if data_correct == True:
            data_objects.active_user = True
            data_objects.active_auth_level = data_objects.user_logged_in['auth_level']
            main_page.open_mainpage()
            if self.checkBox.isChecked() == True:
                self.remember_user = [data_objects.user_logged_in]
                with open("remember_me.txt", "w", encoding="utf-8") as f:
                    f.writelines(json.dumps(self.remember_user, default=str))
            else:
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.pushButton.setDisabled(True)
                self.pushButton_2.setDisabled(True)
                with open("remember_me.txt", "w", encoding="utf-8") as f:
                    f.writelines(json.dumps([], default=str))
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
