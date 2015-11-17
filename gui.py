import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget, QSlider, QLabel, QLineEdit, QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import pickle

from instabot import *

class InstaBotGui(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):

        login = QLabel('Login')
        password = QLabel('Password')
        mtags = QLabel('Hashtags')
        taginfo = QLabel('Input like this #tag1, #tag2. Not more then 5.')
        self.nLikes = QLabel('Likes = 300', self)
        self.putLikes = QLabel('Put likes = 0', self)
        self.putLikes.hide()

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.valueChanged[int].connect(self.changeValue)

        sbtn = QPushButton('Start', self)
        sbtn.resize(90,10)
        sbtn.clicked.connect(self.sbtnHandler)

        self.loginEdit = QLineEdit()
        self.passwordEdit = QLineEdit()
        self.tagsEdit = QLineEdit()



        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(login, 1, 0)
        grid.addWidget(self.loginEdit, 1, 1)
        grid.addWidget(password, 2, 0)
        grid.addWidget(self.passwordEdit, 2, 1)
        grid.addWidget(mtags, 3, 0)
        grid.addWidget(self.tagsEdit, 3, 1)
        grid.addWidget(taginfo, 4, 1)
        grid.addWidget(self.nLikes, 5, 0)
        grid.addWidget(self.sld, 5, 1)
        grid.addWidget(sbtn, 6, 0)
        grid.addWidget(self.putLikes, 6,1)

        self.setLayout(grid)


        self.resize(350, 200)
        self.center()
        self.setWindowTitle('InstaBot')
        self.setWindowIcon(QIcon('logo.png'))
    
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Alert',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def changeValue(self, value):
        self.nLikes.setText('Likes = '+str(300+value*7))

    def saveParams(self, login, password, tags):
        data = {
            'l': login,
            'p': password,
            't': tags
        }
        with open('data.pickle', 'wb') as file:
            pickle.dump(data, file)

    def loadParams(self):

        # try:
        with open('data.pickle', 'rb') as file:
            data_new = pickle.load(file)
            print(data_new)
            self.loginEdit.setText(data_new.get('l'))
            self.passwordEdit.setText(data_new.get('p'))
            self.tagsEdit.setText(data_new.get('t'))
        # except:
        #     pass

    def sbtnHandler(self):

        if (self.loginEdit.text() != '') and (self.passwordEdit.text() != '') and (self.tagsEdit.text() != ''):
            a = 300 +(self.sld.value()*7)
            print(a)
            self.saveParams(self.loginEdit.text(), self.passwordEdit.text(), self.tagsEdit.text())
            instaBot(self.loginEdit.text(), self.passwordEdit.text(), self.tagsEdit.text(), a)
        else:
            self.allert = QMessageBox()
            self.allert.setWindowTitle('Error')
            self.allert.setWindowIcon(QIcon('logo.png'))
            self.allert.setText('Complete all fields')
            self.allert.exec()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    bot = InstaBotGui()
    bot.loadParams()
    sys.exit(app.exec_())  