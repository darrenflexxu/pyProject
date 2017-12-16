# ！/usr/bin/env python
# _*_coding:utf-8_*_
import sys

from PyQt5 import QtWidgets

from MyWindow import MyWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    new = MyWindow()
    new.show()
    sys.exit(app.exec())