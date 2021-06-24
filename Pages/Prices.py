import numpy
import pyqtgraph
from PyQt5 import Qt
from PyQt5.QtWidgets import *
from pyqtgraph import AxisItem

from UI.Pages.Graphs.IntraDayClose import IntraDayClose
from UI.Pages.Graphs.RSIIndicator import RSIIndicator
from UI.Pages.Graphs.Volume import Volume
from UI.Styles import BODY, HEADER, BUY_BUTTON, SELL_BUTTON, Refresh_BUTTON
from UI.util.Stock import *
from UI.util.api import buy_share, sell_share, get_ticker_intra_day


class TimeAxisItem(pyqtgraph.AxisItem):
    def __init__(self, xdict, *args, **kwargs):
        AxisItem.__init__(self, *args, **kwargs)
        self.x_values = numpy.asarray(list(xdict.keys()))
        self.x_strings = list(xdict.values())

    def tickStrings(self, values, scale, spacing):
        strings = []
        for v in values:
            vs = int(v * scale)
            if vs in self.x_values:
                vstr = self.x_strings[numpy.abs(self.x_values - vs).argmin()]
            else:
                vstr = ""
            strings.append(vstr)
        return strings


class Prices(QWidget):

    def __init__(self, ticker, reload):
        super().__init__()
        # Local Variables
        self.ticker = ticker
        self.reload = reload

        # Set Widget Specific Content
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet(BODY)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 10, 20, 10)
        self.layout.setSpacing(5)
        self.daily_price_graph = None

        # Gather Data
        days, close, volume, rsi = get_intra_day(self.ticker)
        short_days, daily_short_volume = get_daily_short_volume(self.ticker)
        short_days = short_days[-100:]
        daily_short_volume = daily_short_volume[-100:]

        # Create Graph Widgets
        intra_day_close_graph = IntraDayClose(days, close)
        rsi = RSIIndicator(days, rsi)
        volume_graph = Volume("Volume", days, volume)
        short_volume_graph = Volume("Short Volume", short_days, daily_short_volume)

        # Link Widgets
        rsi.setXLink(intra_day_close_graph)
        volume_graph.setXLink(intra_day_close_graph)

        # Draw
        self.draw_header()
        self.layout.addWidget(intra_day_close_graph)
        self.layout.addWidget(rsi)
        self.layout.addWidget(volume_graph)
        self.layout.addWidget(short_volume_graph)

    def draw_header(self):
        # General
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # Header
        header = QLabel(self.ticker)
        header.setAlignment(Qt.Qt.AlignCenter)
        header.setStyleSheet(HEADER)

        # Refresh Button
        refresh_button = QPushButton("Refresh")
        refresh_button.setStyleSheet(Refresh_BUTTON)
        refresh_button.clicked.connect(lambda: get_ticker_intra_day(self.ticker) or self.reload())
        refresh_button.setMaximumWidth(100)
        refresh_button.setFixedHeight(65)

        # Purchase Button
        buy_button = QPushButton("Buy")
        buy_button.setStyleSheet(BUY_BUTTON)
        buy_button.clicked.connect(lambda: buy_share(self.ticker))
        buy_button.setMaximumWidth(100)
        buy_button.setFixedHeight(65)

        # Sell Button
        sell_button = QPushButton("Sell")
        sell_button.setStyleSheet(SELL_BUTTON)
        sell_button.clicked.connect(lambda: sell_share(self.ticker))
        sell_button.setMaximumWidth(100)
        sell_button.setFixedHeight(65)

        # Draw
        layout.addWidget(refresh_button)
        layout.addWidget(header)
        layout.addWidget(buy_button)
        layout.addWidget(sell_button)
        self.layout.addWidget(widget)
