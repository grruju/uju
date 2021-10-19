import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
# ----------------- 추 가 ------------------
from PyQt5.QtWidgets import QTableWidgetItem, QProgressBar
from PyQt5.QtCore import Qt
# ------------------------------------------
class OrderbookWorker(QThread):
    dataSent = pyqtSignal(dict)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True

    def run(self):
        while self.alive:
            data  = pybithumb.get_orderbook(self.ticker, limit=10)
            time.sleep(0.05)
            self.dataSent.emit(data)

    def close(self):
        self.alive = False