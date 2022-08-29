# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from lib import SkillTable, TitleWidget, DataLoader, ColorTable, ColorBar, SkillBar, SearchBar, MessageWidget
import config


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("极略三国辅助工具")
        MainWindow.setWindowIcon(QtGui.QIcon(r'source/window_icon.jpeg'))
        MainWindow.setFixedSize(540, 540)
        self.main_window = MainWindow
        # 菜单栏
        self.menu_bar = QtWidgets.QStatusBar(MainWindow)
        bar = MainWindow.menuBar()
        help = bar.addMenu("帮助")

        action_help = QtWidgets.QAction("介绍", MainWindow)
        action_help.setStatusTip("显示软件介绍")
        help.addAction(action_help)
        action_help.triggered.connect(self.show_help)
        action_version = QtWidgets.QAction("版本号", MainWindow)
        action_version.setStatusTip("显示软件版本信息")
        action_version.triggered.connect(self.show_version)
        help.addAction(action_version)

        # 状态栏
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusBar)

        self.central_widget = QtWidgets.QWidget(MainWindow)

        self.tb_hero = QtWidgets.QTextBrowser(self.central_widget)
        self.tb_hero.setGeometry(QtCore.QRect(20, 400, 210, 90))
        self.tb_skill = QtWidgets.QTextBrowser(self.central_widget)
        self.tb_skill.setGeometry(QtCore.QRect(240, 400, 280, 90))
        MainWindow.setCentralWidget(self.central_widget)

        self.init_titles()
        self.init_skill_bar()
        self.init_skill_table()
        self.init_color_bar()
        self.init_color_table()
        self.init_search_bar()

        self.skill_table.connect_skill_bar(self.skill_bar)
        self.skill_table.connect_skill_description(self.tb_skill)
        self.skill_bar.connect_table(self.skill_table)
        self.skill_bar.connect_color_bar(self.color_bar)
        self.skill_bar.connect_color_table(self.color_table)
        self.skill_bar.connect_hero_description(self.tb_hero)
        self.search_bar.connect_skill_table(self.skill_table)

    def init_titles(self):
        # 设置各模块标题
        self.label1 = TitleWidget.TitleLabel(self.central_widget, "配置技能")
        self.label1.setGeometry(QtCore.QRect(70, 10, 110, 30))
        self.label2 = TitleWidget.TitleLabel(self.central_widget, "可搭配技能")
        self.label2.setGeometry(QtCore.QRect(310, 10, 140, 30))
        self.label3 = TitleWidget.TitleLabel(self.central_widget, "刷珠武将")
        self.label3.setGeometry(QtCore.QRect(70, 360, 110, 30))
        self.label4 = TitleWidget.TitleLabel(self.central_widget, "技能描述")
        self.label4.setGeometry(QtCore.QRect(310, 360, 140, 30))

    def init_skill_bar(self):
        self.skill_bar = SkillBar.SkillBar(self.central_widget)

    def init_color_bar(self):
        self.color_bar = ColorBar.ColorBar(self.central_widget)

    def init_color_table(self):
        self.color_table = ColorTable.ColorTable(self.central_widget)

    def init_search_bar(self):
        self.search_bar = SearchBar.SearchBar(self.central_widget)

    def init_skill_table(self):
        # 设置可搭配技能列表
        config.data = DataLoader.load_data('source/skill.xlsx')
        self.skill_table = SkillTable.SkillTable(self.central_widget)

    def show_help(self):
        message_box = MessageWidget.CcMsgBox()
        text = "操作步骤：\n" \
               "1、点击7个按钮中的任意一个选择技能槽。\n" \
               "2、点击列表项设置技能。\n" \
               "3、系统将自动更新色链、色谱和成就武将信息。\n" \
               "4、切换技能槽时列表自动更新可配置技能。\n" \
               "补充：\n" \
               "1、白色珠表示任意珠子，其他颜色与游戏相同。\n" \
               "2、红色文字表示技能无法通过成就获得。\n" \
               "3、按照色链搜索时，需严格遵守”红黄绿蓝“顺序，\n未使用的颜色请用”0“填充。\n" \
               "4、如果需要增加技能或修改技能信息，请直接修改skill.xlsx文件"
        message_box.about(caption=text, window_title="使用说明")

    def show_version(self):
        message_box = MessageWidget.CcMsgBox()
        message_box.about(caption="开发：无恒id\n版本号：v1.0.1", window_title="版本信息")
