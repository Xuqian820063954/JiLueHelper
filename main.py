import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui_window = Ui_MainWindow()
    ui_window.setupUi(window)
    window.show()
    sys.exit(app.exec_())
