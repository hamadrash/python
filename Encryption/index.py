
try :
	from PyQt5.QtWidgets import *
	from PyQt5.QtCore import *
	from PyQt5.QtGui import *
	from PyQt5.uic import loadUiType
	from os import path
	import sys
	noerror = True
except Exception as e:
	noerror = False
	e = str(e)
# import ui File
FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"main.ui"))

# Intiate Ui file

class MainApp(QMainWindow, FORM_CLASS):

	def __init__(self, parent=None):
		super(MainApp,self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.Handle_UI()
		self.Handel_Buttons()
		if noerror != True :

			QMessageBox.warning(self, "Error Importing libraries!", "Error:\n{}".format(e))

	def Handle_UI(self):
		# self = QMainWindow
		self.setWindowTitle('Cipher')
		#self.setFixedSize(900,450)
		self.spinBox.setMaximum(26)
		self.spinBox.setMinimum(1)
		self.spinBox_2.setMaximum(26)
		self.spinBox_2.setMinimum(1)


	def Handel_Buttons(self):
		self.actionExit.triggered.connect(self.exit)
		self.pushButton.clicked.connect(lambda:self.Crypto('e'))
		self.pushButton_2.clicked.connect(lambda: self.Crypto('d'))


	def exit(self):
		QMessageBox.information(self, "Exitting", "See You Next Time (:")
		sys.exit()


	def Crypto(self, mode):
		if mode == 'e':
			text = self.lineEdit_2.text()
			key = self.spinBox.value()
			newtext = self.Ceasar_Cipher(text , key , mode)
			self.lineEdit_4.setText(newtext)
		elif mode == 'd':
			text = self.lineEdit.text()
			key = self.spinBox_2.value()
			newtext = self.Ceasar_Cipher(text, key, mode)
			self.lineEdit_3.setText(newtext)

		
	def Ceasar_Cipher(self, text, key, mode):
		if mode[0].lower() == 'd':
			key = -key
		newtext = ''
		
		for letter in text:
			if letter.isalpha():
				num = ord(letter)
				num += key
				if letter.islower():
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26

				elif letter.isupper():
					if num > ord('Z'):
						num -= 26
					elif num < ord('A'):
						num += 26
				newtext += chr(num)



			else: 
				newtext += letter 
		return newtext

def main():
	app = QApplication(sys.argv)
	window = MainApp()
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()
