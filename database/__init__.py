import sqlite3 as lite
import os
from datetime import datetime, timedelta
import yfinance as yf


def create_connection():
    con = None
    try:
        con = lite.connect('../database/stock.db')
    except lite.Error as e:
        print(e)
    return con


def insert_stock_price(ticker, date: datetime, open_, high, low, close, volume):
    return f"INSERT INTO StockPrices (Stock, Year, Month, Day, Hour, Minute, Open, High, Low, Close, Volume) VALUES ('{ticker}', {date.year}, {date.month}, {date.day}, {date.hour}, {date.minute}, {open_}, {high}, {low}, {close}, {volume});"


def build_insert_stock_price(ticker, date: datetime, open_, high, low, close, volume):
    return f"('{ticker}', {date.year}, {date.month}, {date.day}, {date.hour}, {date.minute}, {open_}, {high}, {low}, {close}, {volume}),"


def update_stock_prices(ticker):
    end_date = datetime.today()
    start_date = end_date - timedelta(59)
    end_date = end_date.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")
    data = yf.download(ticker, start_date, end_date, interval='2m')

    conn = create_connection()
    cur = conn.cursor()
    count = 0
    insert = "INSERT INTO StockPrices (Stock, Year, Month, Day, Hour, Minute, Open, High, Low, Close, Volume) VALUES "
    build = ""
    for date, row in data.iterrows():
        count += 1
        if count > 200:
            count = 0
            cur.execute(insert + build[:-1])
            build = ""
        build += build_insert_stock_price(ticker, date,
                                 row['Open'], row['High'], row['Low'],
                                 row['Adj Close'], row['Volume'])
    if build != "":
        cur.execute(insert + build[:-1])
    conn.commit()


def update_stock(ticker):
    conn = create_connection()
    cur = conn.cursor()

    data = yf.Ticker(ticker)
    sector = data.info['sector']
    industry = data.info['industry']
    dividendYield = data.info['dividendYield']
    if dividendYield is None:
        dividendYield = 0.0
    shortPercentOfFloat = data.info['shortPercentOfFloat']
    sharesOutstanding = data.info['sharesOutstanding']

    insert = f"INSERT INTO Stocks (Stock, Sector, Industry, DividendYield, ShortPercentOfFloat, OutstandingShares) " \
             f"VALUES ('{ticker}', '{sector}', '{industry}', {dividendYield}, {shortPercentOfFloat}, {sharesOutstanding});"

    cur.execute(f"DELETE FROM StockPrices WHERE Stock='{ticker}';")
    cur.execute(f"DELETE FROM Stocks WHERE Stock='{ticker}'; ")
    cur.execute(insert)
    conn.commit()
    conn.close()
    update_stock_prices(ticker)


if __name__ == '__main__':
    ticker = "PINS"
    update_stock(ticker)


# if __name__ == '__main__':
    # conn = create_connection()
    # cur = conn.cursor()
    # for filename in os.listdir('../short_data'):
    #     with open(f'../short_data/{filename}') as file:
    #         for line in file:
    #             if 'Symbol' in line:
    #                 continue
    #             data = line.strip().split(',')
    #             if len(data) < 3:
    #                 continue
    #             cur.execute(f"INSERT INTO Shorts (Stock, ShortVolume, Date) VALUES ('{data[1]}', {data[2]}, '{data[0]}');")
    # conn.commit()

