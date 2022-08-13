import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from lib.SkillTable import SkillTable
from lib.ColorTable import ColorTable
from lib.ColorBar import ColorBar
import re

import config


class SkillBarItem(QPushButton):
    def __init__(self, central_widget):
        super(SkillBarItem, self).__init__(central_widget)
        self.index = config.empty_skill
        self.setText("")
        self.background = ""
        self.foreground = ""
        self.__set_style()

    def set_data(self, index):
        self.index = index
        self.setText(config.data[index][1])
        if config.data[index][7] == 0:
            self.foreground = "color:rgb(255,0,0);"
        else:
            self.foreground = ""
        self.__set_style()

    def set_selected(self):
        self.background = "background:rgb(200,200,200);"
        self.__set_style()
        self.setChecked(True)

    def set_unselected(self):
        self.background = ""
        self.__set_style()
        self.setChecked(False)

    def __set_style(self):
        self.setStyleSheet(self.background + self.foreground)

    def clear(self):
        self.index = config.empty_skill
        self.setText("")


class SkillBar:
    def __init__(self, central_widget):
        # 设置配置技能列表
        self.btn_skills = []
        for i in range(7):
            btn = SkillBarItem(central_widget)
            btn.setGeometry(QtCore.QRect(20 + 70 * (i % 3), 50 + 30 * (i // 3), 70, 30))
            self.btn_skills.append(btn)
        # 连接槽函数
        self.btn_skills[0].clicked.connect(lambda: self.switch_button(0))
        self.btn_skills[1].clicked.connect(lambda: self.switch_button(1))
        self.btn_skills[2].clicked.connect(lambda: self.switch_button(2))
        self.btn_skills[3].clicked.connect(lambda: self.switch_button(3))
        self.btn_skills[4].clicked.connect(lambda: self.switch_button(4))
        self.btn_skills[5].clicked.connect(lambda: self.switch_button(5))
        self.btn_skills[6].clicked.connect(lambda: self.switch_button(6))
        # 设置当前选择的技能
        self.cur_button = -1
        # 设置清除当前按钮
        self.btn_clear = QPushButton(central_widget)
        self.btn_clear.setGeometry(QtCore.QRect(90, 110, 70, 30))
        self.btn_clear.setText("清除当前")
        self.btn_clear.clicked.connect(self.clear)
        # 设置全部清除按钮
        self.btn_clear_all = QPushButton(central_widget)
        self.btn_clear_all.setGeometry(QtCore.QRect(160, 110, 70, 30))
        self.btn_clear_all.setText("清除全部")
        self.btn_clear_all.clicked.connect(self.clear_all)

    def connect_table(self, table: SkillTable):
        self.table = table

    def connect_color_bar(self, color_bar: ColorBar):
        self.color_bar = color_bar

    def connect_color_table(self, color_table: ColorTable):
        self.color_table = color_table

    def connect_hero_description(self, hero_description: QTextBrowser):
        self.hero_description = hero_description

    def switch_button(self, i):
        # 更新按钮状态
        if self.cur_button != -1:
            self.btn_skills[self.cur_button].set_unselected()
        self.btn_skills[i].set_selected()
        self.table.update_skill_description(self.btn_skills[i].index)
        # 若切换按钮，则更新技能列表
        flag = self.cur_button != i
        self.cur_button = i
        if flag:
            rest_colors, names, collision = self.get_rest_colors()
            self.table.update_candidate_data(rest_colors, names, collision)
            self.table.update_show_data()
            self.table.update_items()

    def clear(self):
        self.btn_skills[self.cur_button].clear()
        self.table.update_skill_description(config.empty_skill)
        self.update()

    def clear_all(self):
        for item in self.btn_skills:
            item.clear()
        self.update()
        self.table.update_candidate_data(np.array([0, 0, 0, 0]), set(), set())
        self.table.update_show_data()
        self.table.update_items()
        self.table.update_skill_description(config.empty_skill)

    def update(self):
        # 计算所需色链、所需武将
        colors = np.array([0, 0, 0, 0])
        heros = set()
        count = 0
        for item in self.btn_skills:
            if item.index == config.empty_skill:
                continue
            count += 1
            data_item = config.data[item.index]
            # 武将不为空且为成就武将
            if data_item[0] != "" and data_item[7] == 1:
                heros.add(data_item[0])
            # 更新色链
            for i in range(4):
                colors[i] = max(colors[i], data_item[i + 2])
        # 更新色链需求
        self.color_bar.update(colors)
        # 更新色链表
        self.color_table.update(colors, count)
        # 更新武将说明
        heros = list(heros)
        heros.sort()
        text = ""
        for hero in heros:
            text += hero + " "
        self.hero_description.setText(text)
        return colors

    def get_rest_colors(self):
        colors = np.array([0, 0, 0, 0])
        names = set()
        collision = set()
        for i in range(7):
            if i != self.cur_button and self.btn_skills[i].index != config.empty_skill:
                data_item = config.data[self.btn_skills[i].index]
                names.add(data_item[1])
                if type(data_item[6]) != "无":
                    collision_skills = set(re.findall(r'.{%d}' % 2, data_item[6]))
                    for collision_skill in collision_skills:
                        collision.add(collision_skill)
                for j in range(4):
                    colors[j] = max(colors[j], data_item[j + 2])
        return colors, names, collision
