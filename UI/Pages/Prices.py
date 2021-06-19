import numpy
import pyqtgraph
from PyQt5 import Qt
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, BarGraphItem, AxisItem, mkPen

from UI.Styles import BODY, HEADER, Colors, BUY_BUTTON, SELL_BUTTON, Refresh_BUTTON
from UI.util.Stock import *
from database import update_stock
from database.push_db import buy_stock, sell_stock


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
        self.ticker = ticker
        self.reload = reload

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet(BODY)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 10, 20, 10)
        self.layout.setSpacing(5)
        self.daily_price_graph = None

        self.days = dict(enumerate(get_daily_dates(self.ticker)))
        self.daily_close = get_daily_close(self.ticker)
        self.daily_rsi = get_daily_rsi(self.ticker)
        self.daily_volume = get_daily_volume(self.ticker)

        self.draw_header()
        self.draw_daily_chart()
        self.draw_rsi_chart()
        self.draw_volume_chart()
        self.draw_short_volume_graph()

    def draw_header(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        header = QLabel(self.ticker)
        header.setAlignment(Qt.Qt.AlignCenter)
        header.setStyleSheet(HEADER)

        refresh_button = QPushButton("Refresh")
        refresh_button.setStyleSheet(Refresh_BUTTON)
        refresh_button.clicked.connect(lambda: update_stock(self.ticker) or self.reload())
        refresh_button.setMaximumWidth(100)
        refresh_button.setFixedHeight(65)

        buy_button = QPushButton("Buy")
        buy_button.setStyleSheet(BUY_BUTTON)
        buy_button.clicked.connect(lambda: buy_stock(self.ticker, self.daily_close[-1]))
        buy_button.setMaximumWidth(100)
        buy_button.setFixedHeight(65)

        sell_button = QPushButton("Sell")
        sell_button.setStyleSheet(SELL_BUTTON)
        sell_button.clicked.connect(lambda: sell_stock(self.ticker, self.daily_close[-1]))
        sell_button.setMaximumWidth(100)
        sell_button.setFixedHeight(65)

        layout.addWidget(refresh_button)
        layout.addWidget(header)
        layout.addWidget(buy_button)
        layout.addWidget(sell_button)
        self.layout.addWidget(widget)

    def draw_daily_chart(self):
        string_axis = TimeAxisItem(self.days, orientation='bottom')
        self.daily_price_graph = PlotWidget(axisItems={'bottom': string_axis})
        self.daily_price_graph.setStyleSheet(f"border: 2px solid {Colors.C4};")
        self.daily_price_graph.setBackground((0, 0, 0, 1))
        self.daily_price_graph.getAxis('left').setTextPen(Colors.C4)
        self.daily_price_graph.getAxis('bottom').setTextPen(Colors.C4)
        self.daily_price_graph.hideButtons()
        self.daily_price_graph.setTitle(f"<span style=\"color: {Colors.C4}\">2 Minute Chart</span>")
        self.daily_price_graph.setXRange(len(self.days.items()) - 7, len(self.days.items()))

        self.daily_price_graph.setMouseEnabled(x=True, y=False)
        self.daily_price_graph.setAspectLocked(False)
        self.daily_price_graph.setAutoVisible(y=1.0)
        self.daily_price_graph.enableAutoRange(axis='y', enable=True)

        self.daily_price_graph.plot(list(self.days.keys()), self.daily_close, pen=mkPen(Colors.C4, width=3))
        self.daily_price_graph.setLimits(xMin=1, xMax=len(self.days.items())+10)
        self.layout.addWidget(self.daily_price_graph)

    def draw_rsi_chart(self):
        string_axis = TimeAxisItem(self.days, orientation='bottom')
        rsi_graph = PlotWidget(axisItems={'bottom': string_axis})
        rsi_graph.setStyleSheet(f"border: 2px solid {Colors.C4};")
        rsi_graph.hideButtons()
        rsi_graph.setMaximumHeight(150)
        rsi_graph.setYRange(0, 110)
        rsi_graph.setBackground((0, 0, 0, 1))
        rsi_graph.getAxis('left').setTextPen(Colors.C4)
        rsi_graph.getAxis('bottom').setTextPen(Colors.C4)
        rsi_graph.setAutoVisible(y=0.01)
        rsi_graph.setTitle(f"<span style=\"color: {Colors.C4}\">Relative Strength Index</span>")
        rsi_graph.enableAutoRange(axis='y', enable=True)

        rsi_graph.setMouseEnabled(x=True, y=False)
        rsi_graph.plot(list(self.days.keys()), self.daily_rsi, pen=mkPen(Colors.C4, width=3))
        rsi_graph.setLimits(xMin=1, xMax=len(self.days.items())+10)
        rsi_graph.setXLink(self.daily_price_graph)

        rsi_graph.setXRange(len(self.days.items()) - 7, len(self.days.items()))
        self.layout.addWidget(rsi_graph)

    def draw_volume_chart(self):
        string_axis = TimeAxisItem(self.days, orientation='bottom')
        volume_graph = PlotWidget(axisItems={'bottom': string_axis})
        volume_graph.setStyleSheet(f"border: 2px solid {Colors.C4};")
        volume_graph.hideButtons()
        volume_graph.setMaximumHeight(150)
        volume_graph.setBackground((0, 0, 0, 1))
        volume_graph.getAxis('left').setTextPen(Colors.C4)
        volume_graph.getAxis('bottom').setTextPen(Colors.C4)

        volume_graph.setMouseEnabled(x=True, y=False)
        volume_graph.setAutoVisible(y=True)
        volume_graph.enableAutoRange(axis='y', enable=True)
        volume_graph.setLimits(xMin=1, xMax=len(self.days.items())+10, yMin=0)
        volume_graph.setXLink(self.daily_price_graph)
        volume_graph.setTitle(f"<span style=\"color: {Colors.C4}\">Volume</span>")

        volume = BarGraphItem(x=list(self.days.keys()), width=0.6, height=self.daily_volume, brush='g')
        volume_graph.addItem(volume)

        volume_graph.setXRange(len(self.days.items()) - 7, len(self.days.items()))
        self.layout.addWidget(volume_graph)

    def draw_short_volume_graph(self):
        days, daily_short_volume = get_daily_short_volume(self.ticker)
        days = dict(enumerate(days))

        string_axis = TimeAxisItem(days, orientation='bottom')
        volume_graph = PlotWidget(axisItems={'bottom': string_axis})
        volume_graph.setStyleSheet(f"border: 2px solid {Colors.C4};")
        volume_graph.hideButtons()
        volume_graph.setMaximumHeight(150)
        volume_graph.setBackground((0, 0, 0, 1))
        volume_graph.getAxis('left').setTextPen(Colors.C4)
        volume_graph.getAxis('bottom').setTextPen(Colors.C4)
        volume_graph.setTitle(f"<span style=\"color: {Colors.C4}\">Short Volume</span>")

        volume_graph.setMouseEnabled(x=True, y=False)
        volume_graph.setLimits(xMin=1, xMax=len(days.items())+10)

        volume = BarGraphItem(x=list(days.keys()), width=0.6, height=daily_short_volume, brush='g')
        volume_graph.addItem(volume)

        volume_graph.setXRange(len(days.items()) - 7, len(days.items()))
        self.layout.addWidget(volume_graph)