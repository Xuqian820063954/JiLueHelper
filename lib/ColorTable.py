from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui

from config import shape_style, color_list, check_color_mode


class ColorTable:
    def __init__(self, central_widget):
        self.items = []
        for i in range(9):
            label = QLabel(central_widget)
            label.setText("")
            label.setGeometry(QtCore.QRect(30 + 70 * (i % 3), 190 + 60 * (i // 3), 40, 40))
            label.setStyleSheet(shape_style + color_list["grey"])
            self.items.append(label)

    def update(self, colors, count):
        sort_colors = [(colors[0], "red"), (colors[1], "yellow"), (colors[2], "green"), (colors[3], "blue")]
        sort_colors.sort(key=lambda x: x[0], reverse=True)
        mode = check_color_mode(colors)
        if mode == 1000:
            self.__set_1000(sort_colors[0][1], count)
        elif mode == 1100:
            self.__set_1100(sort_colors[0][1], sort_colors[1][1], count)
        elif mode == 1110:
            self.__set_1110(sort_colors[0][1], sort_colors[1][1], sort_colors[2][1])
        elif mode == 1111:
            self.__set_1111()
        elif mode == 3000:
            self.__set_3000(sort_colors[0][1], count)
        elif mode == 2100:
            self.__set_2100(sort_colors[0][1], sort_colors[1][1], count)
        elif mode == 2200:
            if count <= 6:
                self.__set_2200(sort_colors[0][1], sort_colors[1][1])
            else:
                self.__set_3200(sort_colors[0][1], sort_colors[1][1])
        elif mode == 2210:
            self.__set_2210(sort_colors[0][1], sort_colors[1][1], sort_colors[2][1])
        elif mode == 3100:
            self.__set_3100(sort_colors[0][1], sort_colors[1][1])
        elif mode == 3110:
            self.__set_3110(sort_colors[0][1], sort_colors[1][1], sort_colors[2][1])
        elif mode == 3200:
            self.__set_3200(sort_colors[0][1], sort_colors[1][1])
        elif mode == 6000:
            self.__set_6000(sort_colors[0][1], count)
        elif mode == 6100:
            self.__set_61(sort_colors[0][1], sort_colors[1][1])
        else:
            for item in self.items:
                item.setStyleSheet(shape_style + color_list["grey"])

    def __set_1000(self, color1, count):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list[color1])
        self.items[2].setStyleSheet(shape_style + color_list[color1])
        self.items[3].setStyleSheet(shape_style + color_list["white"])
        self.items[4].setStyleSheet(shape_style + color_list["white"])
        self.items[5].setStyleSheet(shape_style + color_list["white"])
        self.items[6].setStyleSheet(shape_style + color_list["white"])
        self.items[7].setStyleSheet(shape_style + color_list["white"])
        self.items[8].setStyleSheet(shape_style + color_list["white"])
        if count == 7:
            self.items[1].setStyleSheet(shape_style + color_list["colour"])
            self.items[4].setStyleSheet(shape_style + color_list["colour"])

    def __set_1100(self, color1, color2, count):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["white"])
        self.items[2].setStyleSheet(shape_style + color_list["white"])
        self.items[3].setStyleSheet(shape_style + color_list[color2])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list[color2])
        self.items[6].setStyleSheet(shape_style + color_list["white"])
        self.items[7].setStyleSheet(shape_style + color_list["white"])
        self.items[8].setStyleSheet(shape_style + color_list[color1])
        if count == 7:
            self.items[1].setStyleSheet(shape_style + color_list["colour"])

    def __set_1110(self, color1, color2, color3):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["white"])
        self.items[2].setStyleSheet(shape_style + color_list["white"])
        self.items[3].setStyleSheet(shape_style + color_list[color2])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list[color2])
        self.items[6].setStyleSheet(shape_style + color_list["white"])
        self.items[7].setStyleSheet(shape_style + color_list[color3])
        self.items[8].setStyleSheet(shape_style + color_list[color1])

    def __set_1111(self):
        self.items[0].setStyleSheet(shape_style + color_list["red"])
        self.items[1].setStyleSheet(shape_style + color_list["colour"])
        self.items[2].setStyleSheet(shape_style + color_list["green"])
        self.items[3].setStyleSheet(shape_style + color_list["yellow"])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list["yellow"])
        self.items[6].setStyleSheet(shape_style + color_list["green"])
        self.items[7].setStyleSheet(shape_style + color_list["blue"])
        self.items[8].setStyleSheet(shape_style + color_list["red"])

    def __set_3000(self, color1, count):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["white"])
        self.items[2].setStyleSheet(shape_style + color_list[color1])
        self.items[3].setStyleSheet(shape_style + color_list["white"])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list["white"])
        self.items[6].setStyleSheet(shape_style + color_list[color1])
        self.items[7].setStyleSheet(shape_style + color_list["white"])
        self.items[8].setStyleSheet(shape_style + color_list[color1])
        if count == 7:
            self.items[1].setStyleSheet(shape_style + color_list["colour"])

    def __set_2100(self, color1, color2, count):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["white"])
        self.items[2].setStyleSheet(shape_style + color_list[color1])
        self.items[3].setStyleSheet(shape_style + color_list[color2])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list[color2])
        self.items[6].setStyleSheet(shape_style + color_list[color1])
        self.items[7].setStyleSheet(shape_style + color_list["white"])
        self.items[8].setStyleSheet(shape_style + color_list[color1])
        if count == 7:
            self.items[1].setStyleSheet(shape_style + color_list["colour"])

    def __set_2200(self, color1, color2):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list[color1])
        self.items[2].setStyleSheet(shape_style + color_list["colour"])
        self.items[3].setStyleSheet(shape_style + color_list[color1])
        self.items[4].setStyleSheet(shape_style + color_list["white"])
        self.items[5].setStyleSheet(shape_style + color_list[color2])
        self.items[6].setStyleSheet(shape_style + color_list["colour"])
        self.items[7].setStyleSheet(shape_style + color_list[color2])
        self.items[8].setStyleSheet(shape_style + color_list[color2])

    def __set_2210(self, color1, color2, color3):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list[color1])
        self.items[2].setStyleSheet(shape_style + color_list["colour"])
        self.items[3].setStyleSheet(shape_style + color_list[color1])
        self.items[4].setStyleSheet(shape_style + color_list[color3])
        self.items[5].setStyleSheet(shape_style + color_list[color2])
        self.items[6].setStyleSheet(shape_style + color_list["colour"])
        self.items[7].setStyleSheet(shape_style + color_list[color2])
        self.items[8].setStyleSheet(shape_style + color_list[color2])

    def __set_3100(self, color1, color2):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["colour"])
        self.items[2].setStyleSheet(shape_style + color_list[color1])
        self.items[3].setStyleSheet(shape_style + color_list["white"])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list["white"])
        self.items[6].setStyleSheet(shape_style + color_list[color1])
        self.items[7].setStyleSheet(shape_style + color_list[color2])
        self.items[8].setStyleSheet(shape_style + color_list[color1])

    def __set_3110(self, color1, color2, color3):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["colour"])
        self.items[2].setStyleSheet(shape_style + color_list[color1])
        self.items[3].setStyleSheet(shape_style + color_list[color2])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list[color2])
        self.items[6].setStyleSheet(shape_style + color_list[color1])
        self.items[7].setStyleSheet(shape_style + color_list[color3])
        self.items[8].setStyleSheet(shape_style + color_list[color1])

    def __set_3200(self, color1, color2):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["colour"])
        self.items[2].setStyleSheet(shape_style + color_list[color1])
        self.items[3].setStyleSheet(shape_style + color_list[color2])
        self.items[4].setStyleSheet(shape_style + color_list["colour"])
        self.items[5].setStyleSheet(shape_style + color_list[color2])
        self.items[6].setStyleSheet(shape_style + color_list[color1])
        self.items[7].setStyleSheet(shape_style + color_list[color2])
        self.items[8].setStyleSheet(shape_style + color_list[color1])

    def __set_6000(self, color1, count):
        self.items[0].setStyleSheet(shape_style + color_list[color1])
        self.items[1].setStyleSheet(shape_style + color_list["white"])
        self.items[2].setStyleSheet(shape_style + color_list[color1])
        self.items[3].setStyleSheet(shape_style + color_list[color1])
        self.items[4].setStyleSheet(shape_style + color_list["white"])
        self.items[5].setStyleSheet(shape_style + color_list[color1])
        self.items[6].setStyleSheet(shape_style + color_list[color1])
        self.items[7].setStyleSheet(shape_style + color_list["white"])
        self.items[8].setStyleSheet(shape_style + color_list[color1])
        if count == 7:
            self.items[1].setStyleSheet(shape_style + color_list["colour"])
            self.items[4].setStyleSheet(shape_style + color_list["colour"])

    def __set_61(self, color1, color2):
        self.items[0].setStyleSheet(shape_style + color_list["colour"])
        self.items[1].setStyleSheet(shape_style + color_list[color2])
        self.items[2].setStyleSheet(shape_style + color_list["colour"])
        self.items[3].setStyleSheet(shape_style + color_list[color1])
        self.items[4].setStyleSheet(shape_style + color_list[color1])
        self.items[5].setStyleSheet(shape_style + color_list[color1])
        self.items[6].setStyleSheet(shape_style + color_list[color1])
        self.items[7].setStyleSheet(shape_style + color_list[color1])
        self.items[8].setStyleSheet(shape_style + color_list[color1])
