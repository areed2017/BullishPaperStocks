from PyQt5 import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from UI.Styles import BODY, PORTFOLIO_CARD, HEADER, HEADER_2, TRANSACTION_CARD, HEADER_3, TABLE_STYLE
from UI.util.Stock import get_change
from database.retrieve_db import get_share_history, get_current_share_price


class TransactionTable(QTableWidget):

    def __init__(self):
        super().__init__()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setMinimumHeight(600)
        self.setStyleSheet(TABLE_STYLE)

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setShowGrid(False)

    def establish_header(self):
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Ticker Symbol', 'Purchase Price', "Gain/Loss"])
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(36)

    def set_data(self, share_history):
        self.establish_header()
        self.setRowCount(len(share_history))

        for i, share in enumerate(share_history):
            price = share['sell_price']
            if price is None:
                price = get_current_share_price(share['stock'])
            change = get_change(share['buy_price'], price) * 100

            stock_widget = QTableWidgetItem(share['stock'])
            buy_widget = QTableWidgetItem(f"${round(share['buy_price'])}")
            change_widget = QTableWidgetItem(f"{round(change, 2)}%")

            stock_widget.setTextAlignment(Qt.Qt.AlignCenter)
            stock_widget.setFont(QFont('', 18))
            buy_widget.setTextAlignment(Qt.Qt.AlignCenter)
            buy_widget.setFont(QFont('', 18))
            change_widget.setTextAlignment(Qt.Qt.AlignCenter)
            change_widget.setFont(QFont('', 18))

            self.setItem(i, 0, stock_widget)
            self.setItem(i, 1, buy_widget)
            self.setItem(i, 2, change_widget)


class Portfolio(QWidget):

    def __init__(self, ticker, reload):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet(BODY)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 0, 10, 0)
        self.account_layout = None
        self.share_history = get_share_history()

        self.account_header()
        self.transaction_window()
        self.layout.addWidget(QLabel())

    def calculate_free_cash(self):
        bank_total = 10000
        for share in self.share_history:
            bank_total -= share['buy_price']
            if share['sell_price'] is not None:
                bank_total += share['sell_price']
        return round(bank_total, 2)

    def calculate_value(self):
        bank_total = 10000
        for share in self.share_history:
            bank_total -= share['buy_price']
            if share['sell_price'] is not None:
                bank_total += share['sell_price']
            else:
                bank_total += get_current_share_price(share['stock'])
        return bank_total

    def account_header(self):
        widget = QWidget()
        self.account_layout = QHBoxLayout(widget)
        self.account_balance_card()
        self.account_value_card()
        self.account_risk_card()
        self.layout.addWidget(widget)

    def account_balance_card(self):
        card = QWidget()
        card.setStyleSheet(PORTFOLIO_CARD)
        card.setFixedHeight(150)
        card.setMinimumWidth(300)
        layout = QVBoxLayout(card)

        header = QLabel("Free Cash")
        header.setAlignment(Qt.Qt.AlignCenter)
        header.setStyleSheet(HEADER)

        value = QLabel(f"${self.calculate_free_cash()}")
        value.setAlignment(Qt.Qt.AlignCenter)
        value.setStyleSheet(HEADER_2)

        layout.addWidget(header)
        layout.addWidget(value)
        self.account_layout.addWidget(card)

    def account_value_card(self):
        card = QWidget()
        card.setStyleSheet(PORTFOLIO_CARD)
        card.setFixedHeight(150)
        card.setMinimumWidth(300)
        layout = QVBoxLayout(card)

        header = QLabel("Portfolio Value")
        header.setAlignment(Qt.Qt.AlignCenter)
        header.setStyleSheet(HEADER)

        value = QLabel(f"${self.calculate_value()}")
        value.setAlignment(Qt.Qt.AlignCenter)
        value.setStyleSheet(HEADER_2)

        layout.addWidget(header)
        layout.addWidget(value)
        self.account_layout.addWidget(card)

    def account_risk_card(self):
        card = QWidget()
        card.setStyleSheet(PORTFOLIO_CARD)
        card.setFixedHeight(150)
        card.setMinimumWidth(300)
        layout = QVBoxLayout(card)

        header = QLabel("Portfolio Risk")
        header.setAlignment(Qt.Qt.AlignCenter)
        header.setStyleSheet(HEADER)

        value = QLabel(f"Low")
        value.setAlignment(Qt.Qt.AlignCenter)
        value.setStyleSheet(HEADER_2)

        layout.addWidget(header)
        layout.addWidget(value)
        self.account_layout.addWidget(card)

    def transaction_window(self):
        label = QLabel("Stock Transactions")
        label.setStyleSheet(HEADER)
        label.setAlignment(Qt.Qt.AlignCenter)

        table = TransactionTable()
        table.set_data(self.share_history)
        self.layout.addWidget(label)
        self.layout.addWidget(table)


        # scroll = QScrollArea()
        # scroll.setFixedHeight(600)
        # scroll.setWidgetResizable(True)
        # scroll.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        #
        # card = QWidget()
        # # card.setStyleSheet(PORTFOLIO_CARD)
        # card.setFixedHeight(800)
        #
        # layout = QVBoxLayout()
        # layout.setAlignment(Qt.Qt.AlignTop)
        # layout.setSpacing(5)
        #
        # for share in self.share_history:
        #     self.transaction_card(layout, share['stock'], share['buy_price'], share['sell_price'])
        #
        # card.setLayout(layout)
        # scroll.setWidget(card)
        #
        #

    def transaction_card(self, layout, stock, buy_price, sell_price):
        card = QWidget()
        card.setStyleSheet(TRANSACTION_CARD)
        card.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        # card.setFixedHeight(100)
        layout_ = QHBoxLayout()
        layout_.setContentsMargins(0, 0, 0, 0)

        header = QLabel(stock)
        header.setStyleSheet(HEADER_3)
        header.setContentsMargins(10, 0, 10, 0)
        # header.setAlignment(Qt.Qt.AlignCenter)

        buy_in = QLabel(f"Bought at:${buy_price}")
        buy_in.setStyleSheet(HEADER_3)
        buy_in.setAlignment(Qt.Qt.AlignCenter)
        buy_in.setContentsMargins(10, 0, 10, 0)

        if sell_price is not None:
            sell = QLabel(f"Sold at: ${sell_price}")
        else:
            sell = QLabel(f"Holding at: ${get_current_share_price(stock)}")
        sell.setStyleSheet(HEADER_3)
        sell.setContentsMargins(10, 0, 10, 0)
        sell.setAlignment(Qt.Qt.AlignRight)

        layout_.addWidget(header)
        layout_.addWidget(buy_in)
        layout_.addWidget(sell)
        card.setLayout(layout_)
        layout.addWidget(card)