# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana_ekran.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowAnaMenu(object):
    def setupUi(self, MainWindowAnaMenu):
        MainWindowAnaMenu.setObjectName("MainWindowAnaMenu")
        MainWindowAnaMenu.resize(613, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindowAnaMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 81, 16))
        self.label_2.setObjectName("label_2")
        self.btn_gonder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gonder.setGeometry(QtCore.QRect(20, 410, 75, 23))
        self.btn_gonder.setObjectName("btn_gonder")
        self.line_ekle = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ekle.setGeometry(QtCore.QRect(20, 480, 181, 20))
        self.line_ekle.setObjectName("line_ekle")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 450, 221, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 30, 81, 16))
        self.label_5.setObjectName("label_5")
        self.txt_gelenk = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_gelenk.setGeometry(QtCore.QRect(20, 60, 341, 221))
        self.txt_gelenk.setObjectName("txt_gelenk")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(230, 480, 61, 21))
        self.btn_add.setObjectName("btn_add")
        self.lbl_message = QtWidgets.QLabel(self.centralwidget)
        self.lbl_message.setGeometry(QtCore.QRect(20, 510, 251, 21))
        self.lbl_message.setText("")
        self.lbl_message.setObjectName("lbl_message")
        self.listarkadas = QtWidgets.QListWidget(self.centralwidget)
        self.listarkadas.setGeometry(QtCore.QRect(380, 60, 201, 341))
        self.listarkadas.setObjectName("listarkadas")
        self.text_mesajgonder = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_mesajgonder.setGeometry(QtCore.QRect(20, 310, 341, 91))
        self.text_mesajgonder.setObjectName("text_mesajgonder")
        MainWindowAnaMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowAnaMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")
        MainWindowAnaMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowAnaMenu)
        self.statusbar.setObjectName("statusbar")
        MainWindowAnaMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowAnaMenu)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAnaMenu)
        MainWindowAnaMenu.setTabOrder(self.btn_gonder, self.line_ekle)

    def retranslateUi(self, MainWindowAnaMenu):
        _translate = QtCore.QCoreApplication.translate
        MainWindowAnaMenu.setWindowTitle(_translate("MainWindowAnaMenu", "ANA MENÜ"))
        self.label.setText(_translate("MainWindowAnaMenu", "Gelen Kutusu"))
        self.label_2.setText(_translate("MainWindowAnaMenu", "Mesaj Gönder"))
        self.btn_gonder.setText(_translate("MainWindowAnaMenu", "Gönder"))
        self.label_4.setText(_translate("MainWindowAnaMenu", "Kullanıcı ekle"))
        self.label_5.setText(_translate("MainWindowAnaMenu", "Arkadaş listesi"))
        self.btn_add.setText(_translate("MainWindowAnaMenu", "Ekle"))
