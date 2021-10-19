from pybithumb import Bithumb
from websocket import *
from pybithumb import WebSocketManager

if __name__ == "__main__":
    wm = WebSocketManager("ticker", ["BTC_KRW"])
    for i in range(10):
        data = wm.get()
        print(data)
    wm.terminate()