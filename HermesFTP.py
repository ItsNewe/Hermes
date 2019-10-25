import sys
import random
from ftplib import FTP
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
							   QVBoxLayout, QWidget, QLineEdit)
from PySide2.QtCore import Slot, Qt

class MyWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.login = QPushButton("Login (anonymous)")
		self.logout = QPushButton("Logout")
		self.goto=QPushButton("Goto dir")
		self.server = QLineEdit("Server")
		self.dir=QLineEdit()
		self.status = QLabel()

		self.server.setAlignment(Qt.AlignCenter)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.login)
		self.layout.addWidget(self.logout)
		self.layout.addWidget(self.goto)
		self.layout.addWidget(self.server)
		self.layout.addWidget(self.dir)
		self.layout.addWidget(self.status)
		self.setLayout(self.layout)

		self.ftp = None
		# Connecting the signal
		self.login.clicked.connect(self.loginSlot)
		self.logout.clicked.connect(self.logoutSlot)
		self.goto.clicked.connect(self.goToDirSlot)
		

	@Slot()
	def loginSlot(self):
		self.ftp=FTP(QLineEdit.text(self.server))
		self.status.setText(self.ftp.login())

	@Slot()
	def goToDirSlot(self):
		self.ftp.cwd(QLineEdit.text(self.dir))
		a = self.ftp.nlst()
		self.status.setText("\n".join(a))
	
	@Slot()
	def logoutSlot(self):
		try:
			self.ftp.quit()
			self.status.setText("Connection closed successfuly")
		except(Exception) as e:
			self.status.setText(f"Error while terminating connecioin: {e}")


if __name__ == "__main__":
	app = QApplication(sys.argv)

	widget = MyWidget()
	widget.resize(800, 600)
	widget.show()

	sys.exit(app.exec_())
