import pybithumb
import time

# tickers = pybithumb.get_tickers()
# print(tickers)


# print(len(tickers))

# price = pybithumb.get_current_price("BTC")
# print(price)

# import time
# while True:
#     price = pybithumb.get_current_price("btc")
#     print(price)
#     time.sleep(1)

tickers = pybithumb.get_tickers()
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker,price)
    time.sleep(0.1)