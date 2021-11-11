import time
import pybithumb
import datetime

def get_target_price(ticker):
    df = pybithumb.get_ohlcv("ETH")
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("ETH")
ma5 = get_yesterday_ma5("ETH")
sel = target_price + (target_price * 0.007)
while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.delta(seconds=10) : 
        target_price = get_target_price("ETH")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    current_price = pybithumb.get_current_price("ETH")
    print('current :' , current_price)
    print('target :' , target_price)
    print('ma5 :', ma5)
    print('sel :', sel)

    time.sleep(1)