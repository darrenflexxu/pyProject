# ！/usr/bin/env python
# _*_coding:utf-8_*_
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QToolTip, QAction, qApp, QFileDialog


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # tooltips
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        # menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        # open
        open_act = QAction(QIcon('open.png'), '&Open', self)
        open_act.setShortcut('Ctrl+O')
        open_act.setStatusTip('Open file')
        open_act.triggered.connect(self.openFile)
        file_menu.addAction(open_act)
        # exit
        exit_act = QAction(QIcon('exit.png'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)
        # tool bar
        self.toolbar = self.addToolBar('File')
        self.toolbar.addAction(open_act)
        self.toolbar.addAction(exit_act)
        # status bar
        self.statusBar()
        # widget
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def openFile(self):
        path = QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files (*);;Text Files (*.txt)")
