import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pybithumb import Bithumb
import pybithumb
import datetime
from PyQt5.QtCore import QThread, pyqtSignal
from bitcoin.volatility import *


now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_yesterday_ma5('ETH')
target_price = get_target_price('ETH')
sel_price = target_price + (target_price * 0.007)
current_price = pybithumb.get_current_price('ETH')

df = pybithumb.get_ohlcv('ETH')
yesterday = df.iloc[-2]

today_open = yesterday['close']
yesterday_high = yesterday['high']
yesterday_low = yesterday['low']
target5 = today_open + (yesterday_high - yesterday_low) * 0.5
target4 = today_open + (yesterday_high - yesterday_low) * 0.45
target3 = today_open + (yesterday_high - yesterday_low) * 0.3

# print(target5)
# print(target4)
# print(target3)


print('now :',now)
print('mid :',mid)
vs = mid + datetime.timedelta(seconds=10)
print('vs :',vs)
if mid < now < mid + datetime.timedelta(seconds=10) :
                    print("자정입니다.")
else:
    print("111")
print('ma5 :',ma5)
print('target_price :',target_price)
print('maxtarget_price :',target_price+(target_price*0.0005))
print('current_price :',current_price)
print('sel_price :',sel_price)
# (current_price == target_price) and (current_price > ma5)

# (current_price > target_price) and (current_price > ma5) and (maxtarget_price > current_price)


# now = datetime.datetime.now()

# print('mid :',mid)
# print('now :',now)
                # if mid =< now < mid + datetime.delta(seconds=10):