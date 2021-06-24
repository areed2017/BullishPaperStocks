from PyQt5.QtWidgets import *

from UI.Pages.Portfolio import Portfolio
from UI.Pages.Prices import Prices
from UI.Styles import BODY


class Body(QWidget):

    def __init__(self, ticker, set_ticker, page, reload):
        super().__init__()
        self.ticker = ticker
        self.set_ticker = set_ticker
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet(BODY)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        if page == "Price":
            self.layout.addWidget(Prices(self.ticker, reload))
        if page == "Portfolio":
            self.layout.addWidget(Portfolio(self.ticker, reload))
        # if page == "Analysis":
        #     self.layout.addWidget(Analysis())
