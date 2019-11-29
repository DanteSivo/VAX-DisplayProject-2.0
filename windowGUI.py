import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(2, 72, 137)) # Set to Sherwin-Williams Blue Blood #024889
        self.setPalette(p)

        # Set image logo to top right corner
        logoLabel = QLabel(self)
        pixmapLogo = QPixmap('images/sprocket150.png')
        logoLabel.setPixmap(pixmapLogo)
        logoLabel.move(20,20)

        # Set Label 1 - Event name
        eventLabel = QLabel(self)
        eventLabel.setStyleSheet("color: rgb(252, 210, 0);")
        eventLabel.setFont(QtGui.QFont('SansSerif', 30))
        eventLabel.setText("Marvel Mondays! Dante \n Avengers Endgame")
        eventLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        eventLabel.setAlignment(Qt.AlignCenter)
        eventLabel.move(170,150)
        # Set Label 2 - Event timing
        timeLabel = QLabel(self)
        timeLabel.setStyleSheet("color: rgb(252, 210, 0);")
        timeLabel.setFont(QtGui.QFont('SansSerif', 30))
        timeLabel.setText("Until: 1:00AM")
        timeLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        timeLabel.setAlignment(Qt.AlignCenter)
        timeLabel.move(220, 300)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())