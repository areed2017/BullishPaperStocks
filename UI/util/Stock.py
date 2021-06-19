import pandas
from numpy import average

from database.retrieve_db import get_close, get_volume, get_shorts

BUFFER = 14


def get_change(yesterday, today):
    a = yesterday
    b = today
    return (b - a) / a


def get_daily_close(ticker):
    days, close = get_close(ticker)
    return close[BUFFER:]


def get_daily_dates(ticker):
    days, close = get_close(ticker)
    return days[BUFFER:]


def get_daily_volume(ticker):
    days, volume = get_volume(ticker)
    return volume[BUFFER:]


def get_daily_rsi(ticker):
    days, close = get_close(ticker)
    rsi = []
    for i in range(BUFFER, len(close)):
        positive = []
        negative = []
        for j in range(BUFFER):
            change = close[i - j] - close[i - j - 1]
            if change > 0:
                positive += [change]
            else:
                negative += [abs(change)]
        pos_avg = average(positive) + 0.0000000000000000000001
        neg_avg = average(negative) + 0.0000000000000000000001
        rsi += [100 - (100 / (1 + pos_avg / neg_avg))]

    return rsi


def get_daily_short_volume(ticker):
    days, data = get_shorts(ticker)
    return days[BUFFER:], data[BUFFER:]

