import sys
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from kayit_ekrani import Ui_MainWindowKayit
from ana_ekran import Ui_MainWindowAnaMenu


class PencereAnaMenu(QMainWindow):
	def __init__(self):
		super().__init__()
		self.anaMenü = Ui_MainWindowAnaMenu()
		self.anaMenü.setupUi(self)

		kim = özgür
		mesaj = "merhaba naber nasıl gidiyor ne yapıyorsun"
		self.anaMenü.listView.addItem(kim, + " " +  mesaj)



if __name__ == "__main__":
	def calistir():
		uyg = QApplication(sys.argv)
		penc = PencereAnaMenu()
		penc.show()
		sys.exit(uyg.exec_())


	calistir()
