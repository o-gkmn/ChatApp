# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit_ekrani.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowKayit(object):
    def setupUi(self, MainWindowKayit):
        MainWindowKayit.setObjectName("MainWindowKayit")
        MainWindowKayit.resize(295, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindowKayit)
        self.centralwidget.setObjectName("centralwidget")
        self.label_mesaj = QtWidgets.QLabel(self.centralwidget)
        self.label_mesaj.setGeometry(QtCore.QRect(0, 410, 271, 31))
        self.label_mesaj.setText("")
        self.label_mesaj.setObjectName("label_mesaj")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 141, 16))
        self.label.setObjectName("label")
        self.kayit_kadi = QtWidgets.QLineEdit(self.centralwidget)
        self.kayit_kadi.setGeometry(QtCore.QRect(20, 150, 241, 20))
        self.kayit_kadi.setObjectName("kayit_kadi")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 61, 16))
        self.label_2.setObjectName("label_2")
        self.buton_kayit = QtWidgets.QPushButton(self.centralwidget)
        self.buton_kayit.setGeometry(QtCore.QRect(90, 370, 81, 31))
        self.buton_kayit.setObjectName("buton_kayit")
        self.kayit_sifre = QtWidgets.QLineEdit(self.centralwidget)
        self.kayit_sifre.setGeometry(QtCore.QRect(20, 270, 241, 20))
        self.kayit_sifre.setObjectName("kayit_sifre")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_3.setObjectName("label_3")
        self.kayit_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.kayit_ad.setGeometry(QtCore.QRect(20, 90, 141, 20))
        self.kayit_ad.setText("")
        self.kayit_ad.setObjectName("kayit_ad")
        self.dogum_tarihi = QtWidgets.QDateEdit(self.centralwidget)
        self.dogum_tarihi.setGeometry(QtCore.QRect(180, 90, 81, 20))
        self.dogum_tarihi.setObjectName("dogum_tarihi")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 60, 71, 16))
        self.label_4.setObjectName("label_4")
        self.kayit_sifreOnay = QtWidgets.QLineEdit(self.centralwidget)
        self.kayit_sifreOnay.setGeometry(QtCore.QRect(20, 330, 241, 20))
        self.kayit_sifreOnay.setObjectName("kayit_sifreOnay")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 141, 16))
        self.label_6.setObjectName("label_6")
        self.kayit_eposta = QtWidgets.QLineEdit(self.centralwidget)
        self.kayit_eposta.setGeometry(QtCore.QRect(20, 210, 241, 20))
        self.kayit_eposta.setObjectName("kayit_eposta")
        MainWindowKayit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowKayit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 21))
        self.menubar.setObjectName("menubar")
        MainWindowKayit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowKayit)
        self.statusbar.setObjectName("statusbar")
        MainWindowKayit.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowKayit)
        QtCore.QMetaObject.connectSlotsByName(MainWindowKayit)

    def retranslateUi(self, MainWindowKayit):
        _translate = QtCore.QCoreApplication.translate
        MainWindowKayit.setWindowTitle(_translate("MainWindowKayit", "KAYIT"))
        self.label.setText(_translate("MainWindowKayit", "Kullanıcı adı:"))
        self.label_2.setText(_translate("MainWindowKayit", "Şifre:"))
        self.buton_kayit.setText(_translate("MainWindowKayit", "Kayıt"))
        self.label_3.setText(_translate("MainWindowKayit", "Ad - Soyad"))
        self.label_4.setText(_translate("MainWindowKayit", "Doğum tarihi"))
        self.label_5.setText(_translate("MainWindowKayit", "Şifre Onay:"))
        self.label_6.setText(_translate("MainWindowKayit", "E-posta"))
