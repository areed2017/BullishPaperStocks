import requests


def get_ticker_intra_day(ticker):
    data = requests.get(f'http://127.0.0.1:8000/{ticker}/intra_day').json()
    return data['data']


def get_ticker_short_data(ticker):
    data = requests.get(f'http://127.0.0.1:8000/{ticker}/shorts').json()
    return data['data']


def get_current_share_price(ticker):
    data = requests.get(f'http://127.0.0.1:8000/{ticker}/price').json()
    return float(data['price'])


def buy_share(ticker):
    data = requests.get(f'http://127.0.0.1:8000/{ticker}/buy_share').json()
    return bool(data['success'])


def sell_share(ticker):
    data = requests.get(f'http://127.0.0.1:8000/{ticker}/sell_share').json()
    return bool(data['success'])