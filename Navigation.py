from PyQt5 import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from Styles import NAVIGATION, BUTTON, BUTTON_SELECTED, SEARCH_BAR


class Navigation(QWidget):
    selected = "Price"

    def __init__(self, ticker, set_ticker, trigger_loading, reload):
        super().__init__()
        self.reload = reload
        self.ticker = ticker
        self.set_ticker = set_ticker
        self.trigger_loading = trigger_loading

        self.search = None
        self.setStyleSheet(NAVIGATION)
        self.setMaximumWidth(300)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.space()
        self.add_search_bar()
        self.space()
        self.add_price_button()
        self.space()
        self.add_portfolio_button()
        self.space()
        # self.add_analysis_button()
        for i in range(15):
            label = QLabel("")
            self.layout.addWidget(label)

        self.logo = QLabel()
        self.logo.setFixedWidth(300)
        self.logo.setFixedHeight(300)
        self.logo.setScaledContents(True)
        self.logo.setPixmap(QPixmap('imgs/logo_square.png'))
        # self.logo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.logo)

    def space(self):
        label = QLabel("")
        self.layout.addWidget(label)

    def change_page(self, page):
        Navigation.selected = page
        self.reload()

    def add_search_bar(self):
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")
        self.search.setStyleSheet(SEARCH_BAR)
        self.search.setAlignment(Qt.Qt.AlignCenter)
        self.search.returnPressed.connect(self.search_enter)
        self.layout.addWidget(self.search)

    def search_enter(self):
        self.trigger_loading()
        ticker = self.search.text().upper()
        self.set_ticker(ticker)
        self.reload()

    def add_price_button(self):
        price = QPushButton("Price")
        price.setMinimumHeight(80)
        price.setStyleSheet(BUTTON_SELECTED if self.selected == "Price" else BUTTON)
        price.clicked.connect(lambda: self.change_page("Price"))
        self.layout.addWidget(price)

    def add_portfolio_button(self):
        shorts = QPushButton("Portfolio")
        shorts.setMinimumHeight(80)
        shorts.setStyleSheet(BUTTON_SELECTED if self.selected == "Portfolio" else BUTTON)
        shorts.clicked.connect(lambda: self.change_page("Portfolio"))
        self.layout.addWidget(shorts)

