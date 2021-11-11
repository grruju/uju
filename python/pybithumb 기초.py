from pybithumb import Bithumb
import time

# tickers = pybithumb.get_tickers()
# print(tickers)


# print(len(tickers))

# price = pybithumb.get_current_price("BTC")
# print(price)

# import time
# while True:
#     price = Bithumb.get_current_price("btc")
#     print(price)
#     time.sleep(1)

# 코인별 현재가 얻기
tickers = Bithumb.get_tickers()                   # 티커 목록을 파이썬 리스트로 얻어옴
# for ticker in ticker                             # 티커 리스트에서 티커를 하나씩 가져온 후 이를 ticker 변수가 바인딩
#     price = Bithumb.get_current_price(ticker)     # get_current_price()함수를 호출해 ticker 변수가 바인딩하는 가상화폐 현재가 호출
#     print(ticker,price)
#     time.sleep(0.1)

# 거래소 거래 정보
# get_market_detail() 24시간 동안의 시가/고가/저가/종가/거래량을 가져오는 함수
# detail = Bithumb.get_market_detail("BTC")
# print("시가 :",detail[0], "고가 :",detail[1], "저가 :",detail[2], "종가 :",detail[3],"거래량 :",detail[4])

# tickers = pybithumb.get_tickers()
# for coin in tickers[:5]:
#     detail = Bithumb.get_market_detail(coin)
#     print('\033[38;2;215;95;215m'+coin+'\033[0m', '( '"시가 :",detail[0],"고가 :",detail[1],"저가 :",detail[2],"종가 :",detail[3],"거래량 :",detail[4],')')
#     time.sleep(0.1)

# for coin in  pybithumb.get_tickers():
#     print(coin, pybithumb.get_market_detail(coin))

# bithumb = Bithumb("d1660c761cb951aad162f1726bfec20e", "b4b6cb16cc70df1b31030d8a8a3521d9")

# status = bithumb.cancel_order('btc')
# print(status)



import pybithumb
import datetime

# orderbook = pybithumb.get_orderbook("BTC")
# bids = orderbook["bids"]

# for bid in bids:
#     price = bid['price']
#     quant = bid['quantity']
#     print("매수호가 : ", price, "매수잔량: ", quant)


# all = pybithumb.get_current_price("ALL") 
# for ticker, data in all.items() :
#     print(ticker, data['closing_price'])

price = {"open": 100, 'high': 150, 'low': 90, 'close': 130}

print("point-2")
try:
    open = price['open1']
except:
    pass
