import math

import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor

import config


class SkillItem(QTableWidgetItem):
    def __init__(self, index):
        super(SkillItem, self).__init__()
        self.index = index
        self.setText(config.data[index][1])
        self.setTextAlignment(QtCore.Qt.AlignCenter)
        # 非成就武将技能字体设红
        if config.data[index][7] == 0:
            self.setForeground(QColor(255, 0, 0))
        else:
            self.setForeground(QColor(0, 0, 0))


class SkillTable(QTableWidget):
    itemExited = QtCore.pyqtSignal(QTableWidgetItem)

    def __init__(self, parent):
        super(SkillTable, self).__init__(parent)
        # 设置表的位置
        self.setGeometry(QtCore.QRect(240, 90, 280, 210))
        # 隐藏表头
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        # 表项不可编辑
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置列宽
        self.setColumnCount(3)
        self.setColumnWidth(0, 86)
        self.setColumnWidth(1, 86)
        self.setColumnWidth(2, 86)
        # 导入数据
        self.candidate_data = list(range(config.data.shape[0]))
        self.show_data = list(range(config.data.shape[0]))
        self.update_items()
        # 关联变量
        self.skill_bar = None
        self.skill_description = None
        # 设置事件
        self.setMouseTracking(True)
        self.itemClicked.connect(self.update_skill_bar)

        self._last_index = QtCore.QPersistentModelIndex()
        self.viewport().installEventFilter(self)
        self.itemEntered.connect(self.update_skill_description)
        self.itemExited.connect(self.handleItemExited)

    def handleItemEntered(self, item):
        item.setBackground(QColor('moccasin'))

    def handleItemExited(self, item):
        item.setBackground(QTableWidgetItem().background())

    def eventFilter(self, widget, event):
        # if widget is self.viewport():
        index = self._last_index
        if event.type() == QtCore.QEvent.MouseMove:
            index = self.indexAt(event.pos())
        elif event.type() == QtCore.QEvent.Wheel:
            index = self.indexAt(event.pos())
        if index != self._last_index:
            row = self._last_index.row()
            column = self._last_index.column()
            item = self.item(row, column)
            if item is not None:
                self.itemExited.emit(item)
            self._last_index = QtCore.QPersistentModelIndex(index)
        return QTableWidget.eventFilter(self, widget, event)

    def connect_skill_bar(self, skill_bar):
        self.skill_bar = skill_bar

    def connect_skill_description(self, skill_description: QTextBrowser):
        self.skill_description = skill_description

    def update_items(self):
        self.clear()
        self.setRowCount(math.ceil(len(self.show_data) / 3))
        for i, index in enumerate(self.show_data):
            self.setItem(i // 3, i % 3, SkillItem(index))

    def update_skill_description(self, item):
        index = -1
        if type(item) is int:
            index = item
        else:
            index = item.index
            item.setBackground(QColor('moccasin'))
        if index == -1:
            self.skill_description.setText("")
            return
        # 武将说明
        hero = "武将：" + config.data[index][0] + "   "
        # 色链说明
        color = "色链：" + str(config.data[index][2]) + "红" + str(config.data[index][3]) + "黄" + \
                str(config.data[index][4]) + "绿" + str(config.data[index][5]) + "蓝"
        # 冲突技能说明
        collision = ""
        if config.data[index][6] != "无":
            collision = "\n冲突技能：" + config.data[index][6]
        # 技能描述
        description = "\n技能描述：" + config.data[index][8]
        self.skill_description.setText(hero + color + description + collision)

    def update_skill_bar(self):
        if self.skill_bar.cur_button != -1:
            self.skill_bar.btn_skills[self.skill_bar.cur_button].set_data(self.currentItem().index)
            self.skill_bar.update()
        # self.button_platte.switch_button(self.button_platte.cur_button + 1)

    def update_candidate_data(self, rest_colors, names, collision):
        self.candidate_data.clear()
        if config.check_color_mode(rest_colors) == 2210 and len(names) == 6:
            return
        for i in range(config.data.shape[0]):
            # 过滤冲突技能和已有的技能
            if config.data[i][1] in names or config.data[i][1] in collision:
                continue
            # 计算加入新技能后的色链需求
            predict_colors = np.array([0, 0, 0, 0])
            for j in range(4):
                predict_colors[j] = max(rest_colors[j], config.data[i][j + 2])
            # 如果存在色谱满足色链需求，则更新候选技能列表
            predict_color_mode = config.check_color_mode(predict_colors)
            if not (predict_color_mode == "X" or (len(names) == 6 and predict_color_mode == 2210)):
                self.candidate_data.append(i)

    def update_show_data(self):
        # 如果没有搜索关键词，打印所有候选技能
        if config.search_text == "":
            self.show_data = self.candidate_data.copy()
            return
        self.show_data.clear()
        for index in self.candidate_data:
            # 按武将搜索
            if config.search_mode == 0 and config.search_text in config.data[index][0]:
                self.show_data.append(index)
            # 按技能名称搜索
            if config.search_mode == 1 and config.search_text in config.data[index][1]:
                self.show_data.append(index)
            # 按色链需求搜索
            if config.search_mode == 2:
                color = [0, 0, 0, 0]
                for i in range(min(len(config.search_text), 4)):
                    color[i] = max(color[i], int(config.search_text[i]))
                if config.data[index][2] <= color[0] and config.data[index][3] <= color[1] and \
                        config.data[index][4] <= color[2] and config.data[index][5] <= color[3]:
                    self.show_data.append(index)
            if config.search_mode == 3 and config.search_text in config.data[index][8]:
                self.show_data.append(index)
