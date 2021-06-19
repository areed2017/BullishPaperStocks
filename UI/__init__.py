from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, \
    QMainWindow, QSizeGrip
import sys

from UI.Body import Body
from UI.Navigation import Navigation
from UI.Styles import BODY
from UI.TopBar import TopBar


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1600, 900)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(f'Stocks')
        self.ticker = "PINS"
        self.loading = False
        self.setStyleSheet(BODY)
        self.reload()

    def set_ticker(self, ticker):
        self.ticker = ticker

    def trigger_loading(self):
        print("Loading")
        self.loading = True

    def reload(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(TopBar(self))

        body_widget = QWidget()
        body_layout = QHBoxLayout(body_widget)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)
        body_layout.addWidget(Navigation(self.ticker, self.set_ticker, self.trigger_loading, self.reload))
        body_layout.addWidget(Body(self.ticker, self.set_ticker, Navigation.selected, self.reload))

        layout.addWidget(body_widget)
        grip = QSizeGrip(self)
        layout.addWidget(grip)

        self.loading = False
        self.setCentralWidget(central_widget)
        self.show()


def open_ui():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    open_ui()
