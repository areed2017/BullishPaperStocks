import requests


def free_cash():
    data = requests.get(f'http://127.0.0.1:8000/account/free_cash').json()
    return float(data['value'])


def get_portfolio():
    data = requests.get(f'http://127.0.0.1:8000/account/portfolio').json()
    for i in range(len(data['data'])):
        data['data'][i]['buy_price'] = float(data['data'][i]['buy_price'])
        if data['data'][i]['sell_price']  is not None:
            data['data'][i]['sell_price'] = float(data['data'][i]['sell_price'])
    return data['data']


def get_portfolio_value():
    data = requests.get(f'http://127.0.0.1:8000/account/portfolio_value').json()
    return float(data['value'])

