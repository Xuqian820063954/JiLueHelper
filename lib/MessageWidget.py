from PyQt5.QtWidgets import *


class CcMsgBox(QMessageBox):
    def __init__(self):
        super(CcMsgBox, self).__init__()

    def about(self, caption, window_title='信息'):  #
        '''
        @param caption: 正文
        @type caption: str
        @param title: 窗口标题
        @type title: str
        '''
        # 修改显示样式
        msg_label = self.findChild(QLabel, "qt_msgbox_label");
        msg_label.setStyleSheet(f"margin: 5;")
        # 移除影响显示左边距的对象
        lay = self.findChild(QGridLayout)
        lay.removeItem(lay.itemAt(0))
        self.addButton(QMessageBox.StandardButton(QMessageBox.Yes))
        self.button(QMessageBox.StandardButton(QMessageBox.Yes)).hide()
        # 设置正文文本
        self.setText(caption)
        # 设置窗口标题
        self.setWindowTitle(window_title)
        # 显示窗口
        self.exec()
