# ch03/03_20.py
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit
from PyQt5.QtCore import *
  
form_class = uic.loadUiType("./python/cobitsearch.ui")[0]
  
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
        price2 = pykorbit.get_current_price("ETH")
        self.lineEdit_2.setText(str(price2))
    
  
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()