import sys
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from kullanıcıgirisForm import Ui_MainWindow
from kayit_ekrani import Ui_MainWindowKayit

class Pencere(QMainWindow):
	def __init__(self):
		super().__init__()
		self.arayüz = Ui_MainWindow()
		self.arayüz.setupUi(self)

		self.penc_kayit = PencereKayıt()

		self.arayüz.buton_giris.clicked.connect(self.giris_yap)
		self.arayüz.buton_kayit.clicked.connect(self.kayit_ekrani)


	def giris_yap(self):
		eposta = self.arayüz.lineposta.text()
		sifre = self.arayüz.linsifre.text()

		dosya = open("kullanici bilgileri", "r")
		satırlar = dosya.readlines()
		for kullanici in satırlar:
			kullanici_bölünmüş = kullanici.split("//")
			keposta = kullanici_bölünmüş[0]
			ksifre = kullanici_bölünmüş[1]
			if keposta == eposta and ksifre == sifre:
				self.arayüz.label_mesaj.setText("Başarıyla giriş yapıldı.")
			elif not eposta or sifre:
				self.arayüz.label_mesaj.setText("Kullanıcı adı ve şifre boş bırakılamaz") 
			else:
				self.arayüz.label_mesaj.setText("Kullanıcı adı yada şifre hatalı.")
		dosya.close()


	def kayit_ekrani(self):
		self.penc_kayit.show()
		

class PencereKayıt(QMainWindow):
	def __init__(self):
		super().__init__()
		self.arayüz_kayit = Ui_MainWindowKayit()
		self.arayüz_kayit.setupUi(self)

		self.arayüz_kayit.buton_kayit.clicked.connect(self.kayit_ol)

	def kayit_ol(self):

		def kontrol(kullanici_adi, kullanici_eposta):
			dosya = open("kullanici bilgileri", "r")
			dosya_satirlar = dosya.readlines()

			for dosya_satir in dosya_satirlar:
				kullanici_bölünmüş = dosya_satir.split("//")
					
				if kullanici_bölünmüş[0] == k_eposta or kullanici_bölünmüş[2] == k_adı:
					return False
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

		if not kontrol_degisken :
			self.arayüz_kayit.label_mesaj.setText("Bu e-posta zaten mevcut.")
		else:
			if sifre == sifre_onay:
				dosya.write("\n" + k_eposta + "//" + sifre + "//" + k_adı + "//" + isim_soyisim + "//" + dogum_gunu)
				self.arayüz_kayit.label_mesaj.setText("Kayıt başarıyla gerçekleşti.")
				dosya.close()
				sleep(1)
				self.penc_giris = Pencere()
				self.penc_giris.show()
			else:
				self.arayüz_kayit.label_mesaj.setText("Şifreler eşleşmiyor.")

	
def calistir():
	uyg = QApplication(sys.argv)
	penc = Pencere()
	penc.show()
	sys.exit(uyg.exec_())

calistir()
