# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_addition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import mainwindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(736, 722)
        Dialog.setStyleSheet("\n"
"background-color: rgb(239, 248, 255);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_trans.png"))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 691, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 90, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 240, 161, 51))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_7.setDragEnabled(False)
        self.lineEdit_7.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 150, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 60, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 241, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(150, 120, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setWrapping(False)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(290, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(150, 300, 161, 61))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_16.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_16.setClearButtonEnabled(False)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(40, 320, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(150, 180, 161, 20))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(150, 210, 161, 21))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(520, 290, 71, 71))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("default-user-image.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 340, 21, 21))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.pushButton_5.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(370, 320, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(370, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(370, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 60, 161, 21))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(480, 90, 161, 21))
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(370, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(480, 120, 161, 21))
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_20.setGeometry(QtCore.QRect(480, 155, 161, 20))
        self.lineEdit_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(370, 140, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(370, 180, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setGeometry(QtCore.QRect(480, 195, 161, 20))
        self.lineEdit_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_22.setGeometry(QtCore.QRect(480, 225, 161, 51))
        self.lineEdit_22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_22.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_22.setClearButtonEnabled(False)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(370, 225, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_33.setFont(font)
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 410, 691, 241))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 90, 161, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 60, 161, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(40, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(40, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(290, 20, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 149, 161, 61))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 120, 161, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(40, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(40, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(370, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(480, 149, 161, 61))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_9.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_9.setClearButtonEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(480, 90, 161, 20))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(370, 170, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(370, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(480, 60, 161, 20))
        self.lineEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(480, 120, 161, 20))
        self.lineEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(370, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda: close_dialog())
        self.pushButton.setGeometry(QtCore.QRect(290, 670, 75, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 670, 75, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.comboBox.addItems(['-','1','2','3','4','5','6','7','8','9','10','11','12'])
        self.comboBox_2.addItems(['-','Ozel', 'Raporlu', 'Karma'])
        self.comboBox_3.addItems(['-','Akademik','Attentioner'])
        self.comboBox_4.addItems(['-','Evet','Hayir'])

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.comboBox_2.currentIndexChanged.connect(self.state_registration)

        def close_dialog():
                self.save_student()
                Dialog.close()

    def save_student(self):
            # sample data to write to file
            mainwindow.one_student = {
                    "name": self.lineEdit.text(),
                    "surname": self.lineEdit_2.text(),
                    "date_of_birth": self.dateEdit.date(),
                    "identity_no": self.lineEdit_4.text(),
                    "school": self.lineEdit_19.text(),
                    "class": self.comboBox.currentText(),
                    "former_support": self.lineEdit_7.text(),
                    "address": self.lineEdit_16.text(),
                    "registeration_type": self.comboBox_2.currentText(),
                    "module": self.comboBox_3.currentText(),
                    "transportation_service": self.comboBox_4.currentText(),
                    "agreed_price": self.lineEdit_20.text(),
                    "registration date": self.dateEdit_2.date(),
                    "notes_problems": self.lineEdit_22.text(),
                    "photo": '-',
                    "mother_name": self.lineEdit_5.text(),
                    "mother_surname": self.lineEdit_3.text(),
                    "mother_phone": self.lineEdit_8.text(),
                    "mother_address": self.lineEdit_6.text(),
                    "father_name": self.lineEdit_17.text(),
                    "father_surname": self.lineEdit_10.text(),
                    "father_phone": self.lineEdit_18.text(),
                    "father_address": self.lineEdit_9.text()
            }
            mainwindow.students.append(mainwindow.one_student)
            # write data to file
            with open("student_data.txt", "w") as f:
                json.dump(mainwindow.students, f)
                mainwindow.one_student = {}

    def state_registration(self):
            if self.comboBox_2.currentIndex()==2:
                self.lineEdit_20.setDisabled(True)
                self.lineEdit_21.setDisabled(True)
            else:
                self.lineEdit_20.setEnabled(True)
                self.lineEdit_21.setEnabled(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Dogum Tarihi"))
        self.label.setText(_translate("Dialog", "Isim"))
        self.label_6.setText(_translate("Dialog", "Varsa Eski Disleksi Egitim Kurumu"))
        self.label_2.setText(_translate("Dialog", "Soyisim"))
        self.label_4.setText(_translate("Dialog", "TC Kimlik No"))
        self.label_13.setText(_translate("Dialog", "Ogrenci Bilgileri"))
        self.label_22.setText(_translate("Dialog", "Adres"))
        self.label_5.setText(_translate("Dialog", "Okul"))
        self.label_7.setText(_translate("Dialog", "Sinif"))
        self.pushButton_5.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_5.setText(_translate("Dialog", "+"))
        self.label_27.setText(_translate("Dialog", "Fotograf Ekle"))
        self.label_28.setText(_translate("Dialog", "Kayit Tipi"))
        self.label_29.setText(_translate("Dialog", "Egitim Modulu"))
        self.label_30.setText(_translate("Dialog", "Servis Kullanimi"))
        self.label_31.setText(_translate("Dialog", "Anlasilan Baslangic Ucreti"))
        self.label_32.setText(_translate("Dialog", "Odeme Miktari (Her 30 Gun Icin)"))
        self.label_33.setText(_translate("Dialog", "Baslangic Notlari ve Sorunlar"))
        self.label_9.setText(_translate("Dialog", "Anne Isim"))
        self.label_11.setText(_translate("Dialog", "Anne Soyisim"))
        self.label_14.setText(_translate("Dialog", "Ebeveyn Bilgileri"))
        self.label_12.setText(_translate("Dialog", "Anne Adres"))
        self.label_10.setText(_translate("Dialog", "Anne Telefon No"))
        self.label_23.setText(_translate("Dialog", "Baba Telefon No"))
        self.label_24.setText(_translate("Dialog", "Baba Adres"))
        self.label_25.setText(_translate("Dialog", "Baba Soyisim"))
        self.label_26.setText(_translate("Dialog", "Baba Isim"))
        self.pushButton.setText(_translate("Dialog", "Ekle"))
        self.pushButton_2.setText(_translate("Dialog", "Vazgec"))

def open_student_addition():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()