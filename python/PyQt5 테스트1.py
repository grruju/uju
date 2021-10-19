import sys
import PyQt5
from PyQt5.QtCore import center
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 위젯 생성 코드
        self.setGeometry(100,200,300,200)
        self.setWindowTitle("Hello Python")
        self.setWindowIcon(QIcon("./python/bitcoin.png"))

        btn = QPushButton("버튼1", self)
        btn.move(10,10)
        btn.clicked.connect(self.btn_clicked)

        btn = QPushButton("버튼2", self)
        btn.move(10,40)

    # 이벤트 처리 코드
    def btn_clicked(self):
        print("버튼 클릭")

# QApplication 객체 생성 및 이벤트 루프 생성 코드
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()