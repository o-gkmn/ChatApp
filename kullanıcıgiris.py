# -*- coding: utf-8 -*-

import sys
from os import remove
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from kullanıcıgirisForm import Ui_MainWindow
from kayit_ekrani import Ui_MainWindowKayit
from ana_ekran import Ui_MainWindowAnaMenu


cevrimici = False


class Pencere(QMainWindow):

    def __init__(self):
        super().__init__()
        self.arayüz = Ui_MainWindow()
        self.arayüz.setupUi(self)

        self.penc_kayit = PencereKayıt()
        self.pen_ana_menu = PencereAnaMenu()

        self.arayüz.buton_giris.clicked.connect(self.giris_yap)
        self.arayüz.buton_kayit.clicked.connect(self.kayit_ekrani_gecis)

    def giris_yap(self):
        eposta = self.arayüz.lineposta.text()
        sifre = self.arayüz.linsifre.text()

        dosya = open("kullanici bilgileri", "r")
        satırlar = dosya.readlines()
        for kullanici in satırlar:
            kullanici_bölünmüş = kullanici.split("//")
            keposta = kullanici_bölünmüş[0]
            ksifre = kullanici_bölünmüş[1]
            kadi = kullanici_bölünmüş[2]

            if keposta == eposta or kadi == eposta and ksifre == sifre:
                self.arayüz.label_mesaj.setText("Başarıyla giriş yapıldı.")
                global cevrimici
                cevrimici = kadi

                def arkadas_yazdir():
                    self.pen_ana_menu.show()
                    self.close()

                    dosya_arkadaslar = open(cevrimici, "r")
                    dosya_satirlar = dosya_arkadaslar.readlines()

                    for dosya_bolunmus in dosya_satirlar:
                        self.pen_ana_menu.anaMenü.listarkadas.addItem(
                            dosya_bolunmus)

                    dosya_arkadaslar.close()

                arkadas_yazdir()
            else:
                self.arayüz.label_mesaj.setText(
                    "Kullanıcı adı yada şifre hatalı.")

        dosya.close()

    def kayit_ekrani_gecis(self):
        self.penc_kayit.show()
        self.close()


class PencereKayıt(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("KAYIT")
        self.arayüz_kayit = Ui_MainWindowKayit()
        self.arayüz_kayit.setupUi(self)

        self.arayüz_kayit.buton_kayit.clicked.connect(self.kayit_ol)

    def kayit_ol(self):

        def kontrol(kullanici_adi, kullanici_eposta):
            dosya = open("kullanici bilgileri", "r")
            dosya_satirlar = dosya.readlines()

            if dosya_satirlar:
                for dosya_satir in dosya_satirlar:
                    kullanici_bölünmüş = dosya_satir.split("//")
                    dosya_eposta = kullanici_bölünmüş[0]
                    dosya_k_adi = kullanici_bölünmüş[2]

                    if dosya_eposta == k_eposta or dosya_k_adi == k_adı:
                        return False
                    else:
                        return True
            else:
                return True

        k_eposta = self.arayüz_kayit.kayit_eposta.text()
        k_adı = self.arayüz_kayit.kayit_kadi.text()
        sifre = self.arayüz_kayit.kayit_sifre.text()
        sifre_onay = self.arayüz_kayit.kayit_sifreOnay.text()
        isim_soyisim = self.arayüz_kayit.kayit_ad.text()
        dogum_gunu = self.arayüz_kayit.dogum_tarihi.text()

        dosya = open("kullanici bilgileri", "a")

        kontrol_degisken = kontrol(k_adı, k_eposta)

        if not kontrol_degisken:
            self.arayüz_kayit.label_mesaj.setText(
                "Bu e-posta veya kullanıcı adı zaten mevcut.")
        else:
            # e-postanın geçerli olup olmadığını kontrol ediyor(1)
            if k_eposta.count("@") and k_eposta.count(".com"):
                # şifrenin ve kullanıcı adının yeterli olup olmadığını kontrol eder(2)
                if len(k_adı) >= 3 and len(sifre) >= 8:
                    # şifre ile şifre onayın eşit olup olmadığını kontrol ediyor(3)
                    if sifre == sifre_onay:

                        dosya.write(k_eposta + "//" + sifre + "//" + k_adı +
                                    "//" + isim_soyisim + "//" + dogum_gunu + "\n")
                        dosya_arkadaslar = open("kullanici bilgileri", "w")

                        self.penc_giris = Pencere()
                        self.penc_giris.show()
                        self.penc_giris.arayüz.label_mesaj.setText(
                            "Kayıt başarıyla gerçekleşti")
                        self.close()
                    else:
                        self.arayüz_kayit.label_mesaj.setText(
                            "Şifreler eşleşmiyor.")  # (3) numaranın hata mesajı
                else:
                    self.arayüz_kayit.label_mesaj.setText(
                        "Kullanıcı adı 3 karakterden, şifre 8 karekterden kısa olamaz")  # (2)
            else:
                self.arayüz_kayit.label_mesaj.setText(
                    "Geçerli bir e-posta adresi giriniz.")  # (1)
        dosya.close()


class PencereAnaMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.setWindowTitle("ANA MENÜ")
		self.anaMenü = Ui_MainWindowAnaMenu()

        self.anaMenü.btn_add.clicked.connect(self.arkadas_ekle)
        self.anaMenü.btn_gonder.clicked.connect(self.mesaj_gonder)
        self.anaMenü.listarkadas.itemDoubleClicked.connect(
            self.uyari_msgbox)
        self.anaMenü.listarkadas.itemClicked.connect(self.get_mesaj)

        def arkadas_ekle(self):
            ekle_kadi = self.anaMenü.line_ekle.text()
            dosya = open("kullanici bilgileri", "r")
            dosya_satirlar = dosya.readlines()

            # Aynı kullanıcıdan iki defa eklememek için arkadaşlık dosyasını kontrol ediyor
            def kontrol(eklenen_kullanici):
                global cevrimici
                dosya = open(cevrimici, "r")
                dosya_satirlar = dosya.readlines()

                if ekle_kadi+"\n" in dosya_satirlar:
                    return False
                else:
                    return True  # Kontrol true dönerse eklenilen kullanıcı dosyada yok

            liste = []
            for kullanici_satirlar in dosya_satirlar:
                kullanici_bölünmüş = kullanici_satirlar.split("//")
                uye_kadi = kullanici_bölünmüş[2]
                # Tüm kullanıcıları bir listeye ekledim. eklenilen kullanıcı eğer bu listede
                liste.append(kullanici_bölünmüş[2])
                # yoksa böyle bir kullanıcı bulunamadı mesajı vericek(line 176)
                global cevrimici

                if ekle_kadi == uye_kadi and ekle_kadi != cevrimici:
                    if kontrol(ekle_kadi) is True:
                        self.anaMenü.listarkadas.addItem(ekle_kadi)
                        self.anaMenü.lbl_message.setText(
                            "{} başarıyla eklendi".format(ekle_kadi))

                        dosya_arkadaslar = open(cevrimici, "a")
                        dosya_arkadaslar.write(ekle_kadi + "\n")
                        dosya_arkadaslar.close()

                    else:
                        self.anaMenü.lbl_message.setText(
                            "Bu kullanıcı zaten ekli")

                elif ekle_kadi == cevrimici:
                    self.anaMenü.lbl_message.setText(
                        "Kendinizi ekleyemezsiniz")

                elif not ekle_kadi in liste:
                    self.anaMenü.lbl_message.setText(
                        "Böyle bir kullanıcı bulunumadı")

        def uyari_msgbox(self):

            def arkadas_sil():
                global cevrimici
                list_sira = self.anaMenü.listarkadas.currentRow()
                silinecek_eleman = self.anaMenü.listarkadas.currentItem().text()

                dosya = open(cevrimici, "r")
                dosya_satirlar = dosya.readlines()
                arkadas_list = []

                for tekrar_list in dosya_satirlar:  # silincek kullanıcı haricinde dosyadan okuduğum kullanıcı adlarını
                    if silinecek_eleman != tekrar_list:  # boş bir listeye ekledim
                        arkadas_list.append(tekrar_list)

                dosya.close()
                # sonra kullanıcının arkadaş dosyasını kaldırdım
                remove(cevrimici)
                # tekrar aynı dosyayı oluşturdum
                dosya_2 = open(cevrimici, "a")

                for dosya_satir in arkadas_list:  # oluşturduğum arkadaş listesini tekrar dosyaya yazdım
                    dosya_2.write(dosya_satir)
                dosya_2.close()

                self.anaMenü.listarkadas.takeItem(list_sira)
                self.anaMenü.txt_gelenk.clear()

            def hangi_buton(buton):  # uyarı penceresinde hangi butona basıldığını kontrol ettim
                if buton.text() == "OK":
                    arkadas_sil()

            silincek_kullanici = self.anaMenü.listarkadas.currentItem().text()
            uyarı = QMessageBox()  # Uyarı mesajı göstermek için message box penceresi oluşturdum
            uyarı.setWindowTitle("Kullanıcı sil")
            uyarı.setText(
                "{} kullanıcısını silmek istediğine emin misin?".format(silincek_kullanici))
            uyarı.setIcon(QMessageBox.Warning)
            uyarı.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            uyarı.buttonClicked.connect(hangi_buton)
            x = uyarı.exec_()

        def mesaj_gonder(self):

            global cevrimici
            gönderici = cevrimici
            # mesaj gönderme kutusunun içindeki texti alıyor
            mesaj = self.anaMenü.text_mesajgonder.toPlainText()
            alici = self.anaMenü.listarkadas.currentItem().text()

            if not alici:
                self.anaMenü.lbl_message.setText("Kullanıcı yok")

            else:
                dosya = open("mesajlar", "a")
                dosya.write(gönderici+"//"+mesaj+"//"+alici+"\n")
                dosya.close()
                self.anaMenü.text_mesajgonder.clear()

        def get_mesaj(self):
            global cevrimici
            self.anaMenü.txt_gelenk.clear()
            secilen_kisi = self.anaMenü.listarkadas.currentItem().text()

            msg = open("mesajlar", "r")
            msg_satirlar = msg.readlines()

            for msg_satir in msg_satirlar:
                if msg_satir == "\n":  # mesaj dosyasında tek elemanlı liste oluşuyordu ve hata veriyordu, onu düzeltti
                    pass

                else:
                    msg_bolunmus = msg_satir.split("//")
                    gönderici = msg_bolunmus[0]
                    mesaj_txt = msg_bolunmus[1]
                    alici = msg_bolunmus[2]

                    if gönderici+"\n" == secilen_kisi and alici == cevrimici+"\n":
                        self.anaMenü.txt_gelenk.append(
                            gönderici + ">>" + mesaj_txt + "\n")


if __name__ == "__main__":
    def calistir():
        uyg = QApplication(sys.argv)
        penc = Pencere()
        penc.show()
        sys.exit(uyg.exec_())

    calistir()
