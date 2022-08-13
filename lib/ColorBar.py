from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from config import background_style, color_list


class ColorBar:
    def __init__(self, central_widget):
        # 设置色链需求
        self.lbl_color1 = QLabel(central_widget)
        self.lbl_color1.setGeometry(QtCore.QRect(50, 150, 25, 25))
        self.lbl_color1.setStyleSheet(background_style + color_list["red"])
        self.lbl_color1.setText("0")
        self.lbl_color1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_color2 = QLabel(central_widget)
        self.lbl_color2.setGeometry(QtCore.QRect(90, 150, 25, 25))
        self.lbl_color2.setStyleSheet(background_style + color_list["yellow"])
        self.lbl_color2.setText("0")
        self.lbl_color2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_color3 = QLabel(central_widget)
        self.lbl_color3.setGeometry(QtCore.QRect(130, 150, 25, 25))
        self.lbl_color3.setStyleSheet(background_style + color_list["green"])
        self.lbl_color3.setText("0")
        self.lbl_color3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_color4 = QLabel(central_widget)
        self.lbl_color4.setGeometry(QtCore.QRect(170, 150, 25, 25))
        self.lbl_color4.setStyleSheet(background_style + color_list["blue"])
        self.lbl_color4.setText("0")
        self.lbl_color4.setAlignment(QtCore.Qt.AlignCenter)

    def update(self, colors):
        self.lbl_color1.setText(str(colors[0]))
        self.lbl_color2.setText(str(colors[1]))
        self.lbl_color3.setText(str(colors[2]))
        self.lbl_color4.setText(str(colors[3]))
