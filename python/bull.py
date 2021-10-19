import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./python/bull.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

'''
라인 5: loadUiType() 함수를 호출해서 Qt Designer로 생성한 bull.ui 파일을 로드합니다.
라인 7: QMainWindow와 form_class를 상속받아 MyWindow 클래스를 정의합니다.
라인 13: MyWindow 객체를 생성합니다.
라인 14: MyWindow 클래스의 show() 메서드로 윈도우를 화면에 그립니다.
'''