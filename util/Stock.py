from numpy import average

from .api import get_ticker_intra_day, get_ticker_short_data

BUFFER = 14


def get_change(yesterday, today):
    a = yesterday
    b = today
    return (b - a) / a


def get_intra_day(ticker):
    data = get_ticker_intra_day(ticker)
    days = []
    close = []
    volume = []
    rsi = []

    for i in range(BUFFER, len(data)):
        day = data[i]
        days += [day['date_time']]
        close += [float(day['close'])]
        volume += [float(day['volume'])]

        # RSI
        positive = []
        negative = []
        for j in range(BUFFER):
            change = float(data[i - j]['close']) - float(data[i - j - 1]['close'])
            if change > 0:
                positive += [change]
            else:
                negative += [abs(change)]
        pos_avg = average(positive) + 0.0000000000000000000001
        neg_avg = average(negative) + 0.0000000000000000000001
        rsi += [100 - (100 / (1 + pos_avg / neg_avg))]

    return days, close, volume, rsi


def get_daily_short_volume(ticker):
    data = get_ticker_short_data(ticker)
    days = []
    volume = []

    for day in data:
        days += [day['date']]
        volume += [day['volume']]

    return days, volume

