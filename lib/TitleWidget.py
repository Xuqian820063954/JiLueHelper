from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class TitleLabel(QLabel):
    def __init__(self, parent, text):
        super(TitleLabel, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setText(text)
