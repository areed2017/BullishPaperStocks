import sqlite3 as lite
from datetime import datetime


def create_connection():
    con = None
    try:
        con = lite.connect('../database/stock.db')
    except lite.Error as e:
        print(e)
    return con


def get_share_history():
    cur = create_connection().cursor()
    cur.execute(f"SELECT * FROM Portfolio ORDER BY id DESC;")
    rows = cur.fetchall()
    data = []
    for row in rows:
        data += [{
            'stock': row[1],
            'buy_price': row[2],
            'sell_price': row[3],
        }]

    return data


SHARE_PRICES = {}


def get_current_share_price(ticker):
    global SHARE_PRICES
    if ticker in SHARE_PRICES:
        return SHARE_PRICES[ticker]

    cur = create_connection().cursor()
    cur.execute(f"SELECT * FROM StockPrices WHERE stock='{ticker}' ORDER BY id DESC LIMIT 1;")
    data = cur.fetchone()
    SHARE_PRICES[ticker] = data[10]
    return data[10]


def get_shorts(ticker):
    cur = create_connection().cursor()
    cur.execute(f"SELECT * FROM Shorts WHERE stock='{ticker}';")
    rows = cur.fetchall()
    days = []
    data = []
    for row in rows:
        days += [datetime.strptime(row[3], '%Y%m%d')]
        data += [row[2]]

    return days, data


def get_close(ticker):
    cur = create_connection().cursor()
    cur.execute(f"SELECT * FROM StockPrices WHERE stock='{ticker}';")
    rows = cur.fetchall()

    days = []
    close = []
    for row in rows:
        days += [datetime(year=row[2], month=row[3], day=row[4], hour=row[5], minute=row[6])]
        close += [row[10]]

    return days, close


def get_volume(ticker):
    cur = create_connection().cursor()
    cur.execute(f"SELECT * FROM StockPrices WHERE stock='{ticker}';")
    rows = cur.fetchall()

    days = []
    volume = []
    for row in rows:
        days += [datetime(year=row[2], month=row[3], day=row[4], hour=row[5], minute=row[6])]
        volume += [row[11]]

    return days, volume

