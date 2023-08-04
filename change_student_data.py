# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_student_data.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

import connect_database
from PyQt5.QtCore import QDate
import data_objects
import date_consistency
import main_page
import deactivate_student


experience_list = []
salary_paid = []
salary_unpaid = []
new_state = ''
deactivation_mode = ''
payment_date_options = []

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 897)
        Dialog.setStyleSheet("background-color: rgb(0, 52, 77);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 70, 691, 521))
        self.frame.setStyleSheet("color: rgb(255, 230, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 70, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 130, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_4.setFont(font)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 251, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(150, 330, 161, 61))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_16.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_16.setClearButtonEnabled(False)
        self.lineEdit_16.setObjectName("lineEdit_16")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_16.setFont(font)
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(40, 350, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(150, 160, 161, 20))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_19.setFont(font)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(150, 190, 161, 21))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(520, 270, 71, 71))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("default-user-image.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(569, 319, 21, 21))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-color: rgb(255, 230, 207);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_5.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_5.setFont(font)
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(370, 300, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(370, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(370, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_29.setObjectName("label_29")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 40, 161, 21))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_2.setFont(font)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(480, 70, 161, 21))
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_3.setFont(font)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(370, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_30.setObjectName("label_30")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(480, 100, 161, 21))
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_4.setObjectName("comboBox_4")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_4.setFont(font)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_20.setGeometry(QtCore.QRect(480, 135, 161, 20))
        self.lineEdit_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_20.setObjectName("lineEdit_20")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_20.setFont(font)
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(370, 120, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(370, 160, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_22.setGeometry(QtCore.QRect(480, 205, 161, 51))
        self.lineEdit_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_22.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_22.setClearButtonEnabled(False)
        self.lineEdit_22.setObjectName("lineEdit_22")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_22.setFont(font)
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(370, 205, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(150, 100, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.dateEdit.setFont(font)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setGeometry(QtCore.QRect(480, 170, 161, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.dateEdit_2.setFont(font)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setGeometry(QtCore.QRect(480, 365, 161, 20))
        self.lineEdit_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_21.setFont(font)
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(370, 350, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(150, 260, 161, 51))
        self.listWidget.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.add_item())
        self.pushButton_6.setGeometry(QtCore.QRect(290, 240, 21, 21))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_6.setFont(font)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.subtract_item())
        self.pushButton_8.setGeometry(QtCore.QRect(150, 240, 21, 21))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_8.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_8.setFont(font)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_23.setGeometry(QtCore.QRect(170, 240, 121, 20))
        self.lineEdit_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_23.setFont(font)
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(40, 410, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_35.setObjectName("label_35")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(150, 410, 161, 21))
        self.comboBox_6.setAutoFillBackground(False)
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_6.setObjectName("comboBox_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_6.setFont(font)
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(370, 400, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setGeometry(QtCore.QRect(480, 410, 161, 21))
        self.comboBox_7.setAutoFillBackground(False)
        self.comboBox_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_7.setObjectName("comboBox_7")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_7.setFont(font)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.paid_to_unpaid())
        self.pushButton_9.setGeometry(QtCore.QRect(150, 440, 161, 21))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_9.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_9.setFont(font)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.unpaid_to_paid())
        self.pushButton_10.setGeometry(QtCore.QRect(480, 440, 161, 21))
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_10.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_10.setFont(font)
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setGeometry(QtCore.QRect(480, 480, 161, 21))
        self.comboBox_8.setAutoFillBackground(False)
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_8.setObjectName("comboBox_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_8.setFont(font)
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(370, 470, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 620, 691, 211))
        self.frame_2.setStyleSheet("color: rgb(255, 230, 207);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 71, 161, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 41, 161, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_5.setFont(font)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(40, 41, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(40, 71, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 130, 161, 61))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_6.setFont(font)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 101, 161, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_8.setFont(font)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(40, 151, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(40, 101, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(370, 101, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(480, 130, 161, 61))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_9.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_9.setClearButtonEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_9.setFont(font)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(480, 71, 161, 20))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_10.setFont(font)
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(370, 151, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(370, 71, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_25.setObjectName("label_25")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(480, 41, 161, 20))
        self.lineEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_17.setObjectName("lineEdit_17")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_17.setFont(font)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(480, 101, 161, 20))
        self.lineEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_18.setObjectName("lineEdit_18")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_18.setFont(font)
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(370, 41, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog())
        self.pushButton.setGeometry(QtCore.QRect(290, 850, 75, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : Dialog.close())
        self.pushButton_2.setGeometry(QtCore.QRect(380, 850, 75, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 610, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:  rgb(255, 230, 207);")
        self.label_15.setObjectName("label_15")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(40, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:  rgb(255, 230, 207);")
        self.label_14.setObjectName("label_14")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(230, 20, 271, 22))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_5.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.delete_student())
        self.pushButton_3.setGeometry(QtCore.QRect(40, 20, 151, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 246, 194);")
        self.pushButton_3.setObjectName("pushButton_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.set_deactive())
        self.pushButton_7.setGeometry(QtCore.QRect(540, 20, 151, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 246, 194);")
        self.pushButton_7.setObjectName("pushButton_7")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_7.setFont(font)
        self.comboBox_7.setEditable(True)
        self.comboBox_6.setEditable(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        date_consistency.convert_dates_in_list(data_objects.students)
        # write data to file
        with open("student_data.txt", "w", encoding="utf-8") as f:
                f.writelines(json.dumps(data_objects.students, default=str))

        def close_dialog():
            self.data_save()
            Dialog.close()

        with open('student_data.txt', 'r', encoding="utf-8") as f:
                data_objects.students = json.load(f)

        with open('student_data.txt', 'r', encoding="utf-8") as f:
                data_objects.students = json.load(f)

        self.comboBox_5.currentTextChanged.connect(self.combo_changed)
        self.comboBox_5.setCurrentIndex(1)
        self.comboBox_5.setCurrentIndex(0)


        for i in range(1, 29):
                payment_date_options.append(str(i))
        self.comboBox_8.addItems(payment_date_options)

        self.comboBox.addItems(['-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
        self.comboBox_2.addItems(['-', 'Ozel', 'Raporlu', 'Karma'])
        self.comboBox_3.addItems(['-', 'Akademik', 'Attentioner'])
        self.comboBox_4.addItems(['-', 'Evet', 'Hayir'])


        for student in data_objects.students:
                self.comboBox_5.addItem(student['name'] + ' ' + student['surname'])
                self.comboBox_5.model().sort(0)
        if len(data_objects.students) > 1:
                self.comboBox_5.setCurrentIndex(1)
                self.comboBox_5.setCurrentIndex(0)

    def combo_changed(self):
            self.listWidget.clear()
            self.comboBox_7.clear()
            self.comboBox_6.clear()
            for student in data_objects.students:
                    if self.comboBox_5.currentText() == student['name'] + ' ' + student['surname']:
                            if 'Aktif' in student['status']:
                                    self.pushButton_7.setText('Deaktive Et')
                            else:
                                    self.pushButton_7.setText('Aktive Et')
                            try:
                                    self.comboBox_7.clear()
                                    self.comboBox_6.clear()
                                    # self.label_8.setPixmap(student['photo'])
                                    self.lineEdit.setText(student['name'])
                                    self.lineEdit_2.setText(student['surname'])
                                    self.dateEdit.setDate(
                                            datetime.strptime(student['date_of_birth'], '%d-%m-%Y').date())
                                    self.lineEdit_4.setText(student['identity_no'])
                                    self.lineEdit_19.setText(student['school'])
                                    self.comboBox.setCurrentText(student['class'])
                                    self.dateEdit_2.setDate(
                                            datetime.strptime(student['registration date'], '%d-%m-%Y').date())
                                    self.listWidget.addItems(student['former_support'])
                                    self.comboBox_6.addItems(student['paid_debt'])
                                    self.lineEdit_16.setText(student['address'])
                                    self.comboBox_2.setCurrentText(student['registeration_type'])
                                    self.comboBox_3.setCurrentText(student['module'])
                                    self.comboBox_7.addItems(student['unpaid_debt'])
                                    self.comboBox_8.setCurrentText(student['monthly_payment_date'])
                                    self.comboBox_4.setCurrentText(student['transportation_service'])
                                    self.lineEdit_20.setText(student['agreed_price'])
                                    self.lineEdit_22.setText(student['notes_problems'])
                                    self.lineEdit_5.setText(student['mother_name'])
                                    self.lineEdit_3.setText(student['mother_surname'])
                                    self.lineEdit_8.setText(student['mother_phone'])
                                    self.lineEdit_6.setText(student['mother_address'])
                                    self.lineEdit_17.setText(student['father_name'])
                                    self.lineEdit_10.setText(student['father_surname'])
                                    self.lineEdit_18.setText(student['father_phone'])
                                    self.lineEdit_9.setText(student['father_address'])

                            except IndexError:
                                    pass
                    else:
                            pass

    def set_deactive(self):
            global new_state
            if self.pushButton_7.text() == 'Aktive Et':
                    pass
            else:
                deactivate_student.open_deactivate_student()
            import datetime
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Ogrenciyi Inaktif Et")
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(
                    "Ogrenci statusu degistirelecektir. Kabul ediyor musunuz?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            yesButton = msgBox.button(QMessageBox.Yes)
            yesButton.setText("Evet")
            noButton = msgBox.button(QMessageBox.No)
            noButton.setText("Hayir")
            response = msgBox.exec_()
            for student in data_objects.students:
                    if self.comboBox_5.currentText() == student['name'] + ' ' + student['surname']:
                            # Perform an action based on the user's response
                            if response == QMessageBox.Yes and 'Aktif' in student['status']:
                                    current_date = datetime.date.today()
                                    formatted_date = current_date.strftime("%d-%m-%Y")
                                    new_state = 'Pasif' + '           ' + formatted_date
                                    student['status'] = new_state
                                    self.pushButton_7.setText('Aktive Et')
                                    self.pushButton_7.setDisabled(True)
                            elif response == QMessageBox.Yes and 'Pasif' in student['status']:
                                    current_date = datetime.date.today()
                                    formatted_date = current_date.strftime("%d-%m-%Y")
                                    new_state = 'Aktif' + '           ' + formatted_date
                                    student['status'] = new_state
                                    self.pushButton_7.setText('Deaktive Et')
                                    self.pushButton_7.setDisabled(True)
                            else:
                                    pass


    def delete_student(self):
        try:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Ogrenciyi Sil")
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(
                    "Ogrenci sistemden tamamen silinecektir. Kabul ediyor musunuz?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            yesButton = msgBox.button(QMessageBox.Yes)
            yesButton.setText("Evet")
            noButton = msgBox.button(QMessageBox.No)
            noButton.setText("Hayir")
            response = msgBox.exec_()
            # Perform an action based on the user's response
            if response == QMessageBox.Yes:
                    for student in data_objects.students:
                            if student['name'] + ' ' + student['surname'] == self.comboBox_5.currentText():
                                    del data_objects.students[data_objects.students.index(student)]
                                    data_objects.one_student = {}
                            else:
                                pass
                    self.pushButton_3.setDisabled(True)
            else:
                pass
        except ValueError:
                pass

    def paid_to_unpaid(self):
            item = self.comboBox_6.currentText()
            self.comboBox_6.removeItem(self.comboBox_6.currentIndex())
            self.comboBox_7.addItem(item)
            salary_unpaid.append(item)

    def unpaid_to_paid(self):
            item = self.comboBox_7.currentText()
            self.comboBox_7.removeItem(self.comboBox_7.currentIndex())
            self.comboBox_6.addItem(item)
            salary_paid.append(item)

    def data_save(self):

            msgBox = QMessageBox()
            msgBox.setWindowTitle("Ogrenci Verisi Duzenle")
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(
                    "Girdiginiz bilgileri kontrol ettiyseniz, degisen veriler sisteme kaydedilecektir. Onayliyor musunuz?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            yesButton = msgBox.button(QMessageBox.Yes)
            yesButton.setText("Evet")
            noButton = msgBox.button(QMessageBox.No)
            noButton.setText("Hayir")
            response = msgBox.exec_()
            # Perform an action based on the user's response
            if response == QMessageBox.Yes:
                    self.get_items()
                    import datetime
                    current_date = datetime.date.today()
                    formatted_date = current_date.strftime("%d-%m-%Y")
                    salary_changed = []
                    for student in data_objects.students:
                            if self.comboBox.currentText() == student['name'] + ' ' + student['surname']:
                                    if self.lineEdit_21.text() != '' and self.lineEdit_21.text() != ' ' and self.lineEdit_21.text() != '  ':
                                            salary_changed.append(
                                                    self.lineEdit_21.text() + 'TL' + ' / ' + formatted_date)
                                    else:
                                            salary_changed = student['price_change']
                                    if len(self.lineEdit_28.text()) > 1:
                                            salary_changed.append(
                                                    self.lineEdit_28.text() + 'TL' + ' / ' + formatted_date)
                                    else:
                                            salary_changed = student['price_change']
                            if self.comboBox_5.currentText() == student['name'] + ' ' + student['surname']:
                                    data_objects.students[data_objects.students.index(student)] = {
                                                "name": self.lineEdit.text().title(),
                                                "surname": self.lineEdit_2.text().title(),
                                                "date_of_birth": self.dateEdit.date().toPyDate(),
                                                "identity_no": self.lineEdit_4.text().title(),
                                                "school": self.lineEdit_19.text().title(),
                                                "class": self.comboBox.currentText(),
                                                "former_support": experience_list,
                                                "address": self.lineEdit_16.text().title(),
                                                "registeration_type": self.comboBox_2.currentText(),
                                                "module": self.comboBox_3.currentText(),
                                                "transportation_service": self.comboBox_4.currentText(),
                                                "agreed_price": self.lineEdit_20.text().title(),
                                                "registration date": self.dateEdit_2.date().toPyDate(),
                                                "notes_problems": self.lineEdit_22.text().title(),
                                                "photo": '-',
                                                "mother_name": self.lineEdit_5.text().title(),
                                                "mother_surname": self.lineEdit_3.text().title(),
                                                "mother_phone": self.lineEdit_8.text().title(),
                                                "mother_address": self.lineEdit_6.text().title(),
                                                "father_name": self.lineEdit_17.text().title(),
                                                "father_surname": self.lineEdit_10.text().title(),
                                                "father_phone": self.lineEdit_18.text().title(),
                                                "father_address": self.lineEdit_9.text().title(),
                                                "status": new_state,
                                                "price_change": salary_changed,
                                                "student_schedule": student['student_schedule'],
                                                "student_attended": student['student_attended'],
                                                "student_skipped": student['student_skipped'],
                                                "schedule_changed": student['schedule_changed'],
                                                "schedule_cancelled": student['schedule_cancelled'],
                                                "monthly_payment_date": self.comboBox_8.currentText(),
                                                "paid_debt": salary_paid,
                                                "unpaid_debt": salary_unpaid,
                                                "student_left": deactivation_mode
                                        }

                                    date_consistency.convert_dates_in_list(data_objects.students)
                                    # write data to file
                                    with open("student_data.txt", "w", encoding="utf-8") as f:
                                            f.writelines(json.dumps(data_objects.students, default=str))
                                    with open('student_data.txt', 'r', encoding="utf-8") as f:
                                            data_objects.students = json.load(f)

                                    connect_database.txt_to_csv('student_data.txt', 'student_data.csv')
                                    connect_database.upload_files('student_data.txt')
                                    connect_database.upload_files('student_data.csv')

                            else:
                                    pass

    def add_item(self):
            text = self.lineEdit_23.text()
            self.listWidget.addItem(text)
            self.lineEdit_23.clear()

    def subtract_item(self):
            current_row = self.listWidget.currentRow()
            if current_row != -1:
                    self.listWidget.takeItem(current_row)

    def get_items(self):
            global experience_list
            items = []
            for index in range(self.listWidget.count()):
                    items.append(self.listWidget.item(index).text())
            experience_list = items
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ogrenci Verilerini Duzenle"))
        self.label_3.setText(_translate("Dialog", "Dogum Tarihi"))
        self.label.setText(_translate("Dialog", "Isim"))
        self.label_6.setText(_translate("Dialog", "Eski Ozel Egitim Kurumu"))
        self.label_2.setText(_translate("Dialog", "Soyisim"))
        self.label_4.setText(_translate("Dialog", "TC Kimlik No"))
        self.label_22.setText(_translate("Dialog", "Adres"))
        self.label_5.setText(_translate("Dialog", "Okul"))
        self.label_7.setText(_translate("Dialog", "Sinif"))
        self.pushButton_5.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_5.setText(_translate("Dialog", "+"))
        self.label_27.setText(_translate("Dialog", "Fotograf Ekle"))
        self.label_28.setText(_translate("Dialog", "Kayit Tipi"))
        self.label_29.setText(_translate("Dialog", "Egitim Modulu"))
        self.label_30.setText(_translate("Dialog", "Servis Kullanimi"))
        self.label_31.setText(_translate("Dialog", "Saatlik Ders Ucreti"))
        self.label_32.setText(_translate("Dialog", "Kayit Tarihi"))
        self.label_33.setText(_translate("Dialog", "Baslangic Notlari ve Sorunlar"))
        self.label_34.setText(_translate("Dialog", "Yeni Saatlik Ders Ucreti Ekle"))
        self.pushButton_6.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_6.setText(_translate("Dialog", "+"))
        self.pushButton_8.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_8.setText(_translate("Dialog", "-"))
        self.label_35.setText(_translate("Dialog", "Alinan Odemeler"))
        self.label_36.setText(_translate("Dialog", "Alinmayan Odemeler"))
        self.pushButton_9.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_9.setText(_translate("Dialog", "Secili Odeme Alinmadi"))
        self.pushButton_10.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_10.setText(_translate("Dialog", "Secili Odeme Alindi"))
        self.label_37.setText(_translate("Dialog", "Aylik Odeme Gunu"))
        self.label_9.setText(_translate("Dialog", "Anne Isim"))
        self.label_11.setText(_translate("Dialog", "Anne Soyisim"))
        self.label_12.setText(_translate("Dialog", "Anne Adres"))
        self.label_10.setText(_translate("Dialog", "Anne Telefon No"))
        self.label_23.setText(_translate("Dialog", "Baba Telefon No"))
        self.label_24.setText(_translate("Dialog", "Baba Adres"))
        self.label_25.setText(_translate("Dialog", "Baba Soyisim"))
        self.label_26.setText(_translate("Dialog", "Baba Isim"))
        self.pushButton.setText(_translate("Dialog", "Kaydet"))
        self.pushButton_2.setText(_translate("Dialog", "Vazgec"))
        self.label_15.setText(_translate("Dialog", "  Ebeveyn Bilgileri"))
        self.label_14.setText(_translate("Dialog", "  Ogrenci Bilgileri"))
        self.pushButton_3.setText(_translate("Dialog", "Ogrenciyi Sil"))
        self.pushButton_7.setText(_translate("Dialog", "Deaktive Et"))

def change_student():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()