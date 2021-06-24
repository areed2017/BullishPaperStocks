from PyQt5 import QtGui, Qt
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QBrush, QColor, QLinearGradient
from PyQt5.QtWidgets import *

from Styles import TOP_BAR, Colors, TOP_BAR_BUTTON


class TopBar(QWidget):

    def __init__(self, window):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFixedHeight(45)
        self.setStyleSheet(TOP_BAR)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.title = QLabel()
        self.title.setPixmap(QPixmap('imgs/logo.png'))
        self.title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.title)
        for i in range(20):
            label = QLabel()
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.layout.addWidget(label)

        self.window = window
        self.oldPos = self.pos()
        self.add_buttons()

    def add_buttons(self):
        icon_min = QIcon("imgs/min.png")
        icon_max = QIcon("imgs/max.png")
        icon_close = QIcon("imgs/close.png")

        self.minimize = QToolButton()
        self.minimize.setStyleSheet(TOP_BAR_BUTTON)
        self.minimize.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.minimize.setIcon(icon_min)

        self.maximize = QToolButton()
        self.maximize.setStyleSheet(TOP_BAR_BUTTON)
        self.maximize.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.maximize.setIcon(icon_max)

        close = QToolButton(self)
        close.setStyleSheet(TOP_BAR_BUTTON)
        close.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        close.setIcon(icon_close)

        self.layout.addWidget(self.minimize)
        self.layout.addWidget(self.maximize)
        self.layout.addWidget(close)

        close.clicked.connect(self.close)
        self.maximize.clicked.connect(self.window.showMaximized)
        self.minimize.clicked.connect(self.window.showMinimized)

    def close(self):
        quit()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.window.move(self.window.x() + delta.x(), self.window.y() + delta.y())
        self.oldPos = event.globalPos()
