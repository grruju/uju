# ch03/03_20.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
  
form_class = uic.loadUiType("./python/test.ui")[0]
  
  
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton2.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")
  
  
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()