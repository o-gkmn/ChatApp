# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kullanıcıgirisForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineposta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineposta.setGeometry(QtCore.QRect(20, 180, 211, 20))
        self.lineposta.setObjectName("lineposta")
        self.linsifre = QtWidgets.QLineEdit(self.centralwidget)
        self.linsifre.setGeometry(QtCore.QRect(20, 240, 211, 20))
        self.linsifre.setObjectName("linsifre")
        self.buton_giris = QtWidgets.QPushButton(self.centralwidget)
        self.buton_giris.setGeometry(QtCore.QRect(150, 290, 81, 31))
        self.buton_giris.setObjectName("buton_giris")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 150, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_mesaj = QtWidgets.QLabel(self.centralwidget)
        self.label_mesaj.setGeometry(QtCore.QRect(10, 350, 241, 21))
        self.label_mesaj.setText("")
        self.label_mesaj.setObjectName("label_mesaj")
        self.buton_kayit = QtWidgets.QPushButton(self.centralwidget)
        self.buton_kayit.setGeometry(QtCore.QRect(30, 290, 81, 31))
        self.buton_kayit.setObjectName("buton_kayit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 272, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GİRİŞ"))
        self.buton_giris.setText(_translate("MainWindow", "Giriş"))
        self.label.setText(_translate("MainWindow", "Kullanıcı adı ya da E-posta:"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.buton_kayit.setText(_translate("MainWindow", "Kayıt"))
