
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider,
                             QFrame, QApplication)
from PyQt5.QtGui import QColor, QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
import sys


class FenPrincipal(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("RBG")
        self.resize(500, 300)
        self.initFen()
        self.show()
        print(str(self.rSlider.geometry()))
        print(str(self.gSlider.geometry()))
        print(str(self.bSlider.geometry()))

    def initFen(self):
        mainLayout = QVBoxLayout()

        #configuration du champ de couleur
        font = QFont("Times New Roman", 12)
        frameLayout = QVBoxLayout()
        self.couleur = QFrame()
        self.couleur.setFixedSize(200, 150)
        self.col = QColor(0, 0, 0)
        self.couleur.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        self.staticStr = "Hexadecimal : "
        self.hexValue = QLabel(self.staticStr + ":" + self.getHex(0, 0, 0))
        self.hexValue.setFont(font)
        frameLayout.addWidget(self.couleur)
        frameLayout.addWidget(self.hexValue)
        frameLayout.setAlignment(Qt.AlignCenter)

        #configuration de la personalisation de couleur Rouge
        iSize = QSize(10, 10)
        redLayout = QHBoxLayout()
        rIcon = QLabel()
        rIcon.setPixmap(QPixmap("red.ico").scaled(iSize))
        rLabel = QLabel("Rouge")
        self.rSlider = QSlider(Qt.Horizontal)
        self.rSlider.setMaximum(255)
        self.rSlider.valueChanged.connect(self.changeRed)
        self.rValue = QLabel("0")
        redLayout.addWidget(rIcon)
        redLayout.addWidget(rLabel)
        redLayout.addWidget(self.rSlider)
        redLayout.addWidget(self.rValue)

        #configuration de la personalisation de couleur Vert
        greenLayout = QHBoxLayout()
        gIcon = QLabel()
        gIcon.setPixmap(QPixmap("green.ico").scaled(iSize))
        gLabel = QLabel("Vert")
        self.gSlider = QSlider(Qt.Horizontal)
        self.gSlider.setMaximum(255)
        self.gValue = QLabel("0")
        self.gSlider.valueChanged.connect(self.changeGreen)
        greenLayout.addWidget(gIcon)
        greenLayout.addWidget(gLabel)
        greenLayout.addWidget(self.gSlider)
        greenLayout.addWidget(self.gValue)

        #configuration de la personalisation de couleur Bleu
        blueLayout = QHBoxLayout()
        bIcon = QLabel()
        bIcon.setPixmap(QPixmap("blue.ico").scaled(iSize))
        bLabel = QLabel("Blue")
        self.bSlider = QSlider(Qt.Horizontal)
        self.bSlider.setMaximum(255)
        self.bValue = QLabel("0")
        self.bSlider.valueChanged.connect(self.changeBlue)
        blueLayout.addWidget(bIcon)
        blueLayout.addWidget(bLabel)
        blueLayout.addWidget(self.bSlider)
        blueLayout.addWidget(self.bValue)

        mainLayout.addLayout(frameLayout)
        mainLayout.addLayout(redLayout)
        mainLayout.addLayout(greenLayout)
        mainLayout.addLayout(blueLayout)
        
        self.setLayout(mainLayout)
        
    
    def getHex(self, r, g, b):
        return " #" +str(hex(r))[2:] + str(hex(g))[2:] + str(hex(b))[2:]

    def changeRed(self, val):
        self.rValue.setText(str(val))
        self.col.setRed(val)
        self.couleur.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        r, g, b = self.col.red(), self.col.green(), self.col.blue()
        self.hexValue.setText(self.staticStr + ":" + self.getHex(r, g, b))
    
    def changeGreen(self, val):
        self.gValue.setText(str(val))
        self.col.setGreen(val)
        self.couleur.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        r, g, b = self.col.red(), self.col.green(), self.col.blue()
        self.hexValue.setText(self.staticStr + ":" + self.getHex(r, g, b))
    
    def changeBlue(self, val):
        self.bValue.setText(str(val))
        self.col.setBlue(val)
        self.couleur.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        r, g, b = self.col.red(), self.col.green(), self.col.blue()
        self.hexValue.setText(self.staticStr + ":" + self.getHex(r, g, b))


app = QApplication(sys.argv)
fen = FenPrincipal()
sys.exit(app.exec_())