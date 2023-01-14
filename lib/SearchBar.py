from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui

from lib.SkillTable import SkillTable
import config


class SearchBar:
    def __init__(self, central_widget):
        # 设置搜索范围
        self.cb_search = QComboBox(central_widget)
        self.cb_search.setGeometry(QtCore.QRect(310, 50, 85, 30))
        self.cb_search.addItems(["按武将搜索", "按技能搜索", "按色链搜索", "按描述搜索"])
        self.cb_search.setCurrentIndex(0)
        # 设置搜索框
        self.le_search = QLineEdit(central_widget)
        self.le_search.setGeometry(QtCore.QRect(395, 50, 195, 30))
        self.le_search.setClearButtonEnabled(True)
        self.le_search.setPlaceholderText("请输入武将名称，如刘备")
        # 保存无限制校验器
        self.validator = self.le_search.validator()
        # 绑定事件
        self.cb_search.currentIndexChanged.connect(self.set_search_limit)
        self.cb_search.currentIndexChanged.connect(self.search_skill)
        self.le_search.textEdited.connect(self.search_skill)

    def connect_skill_table(self, skill_table: SkillTable):
        self.skill_table = skill_table

    def set_search_limit(self):
        self.le_search.clear()
        if self.cb_search.currentIndex() == 0:
            self.le_search.setPlaceholderText("请输入武将名称，如刘备")
            self.le_search.setValidator(self.validator)
        elif self.cb_search.currentIndex() == 1:
            self.le_search.setPlaceholderText("请输入技能名称，如大德")
            self.le_search.setValidator(self.validator)
            self.le_search.setMaxLength(2)
        elif self.cb_search.currentIndex() == 2:
            self.le_search.setPlaceholderText("请输入色链需求，如1111")
            self.le_search.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-6]{4}")))
            self.le_search.setMaxLength(4)
        else:
            self.le_search.setPlaceholderText("请输入描述关键词，如装备")
            self.le_search.setValidator(self.validator)

    def search_skill(self):
        config.search_text = self.le_search.text()
        config.search_mode = self.cb_search.currentIndex()
        self.skill_table.update_show_data()
        self.skill_table.update_items()
