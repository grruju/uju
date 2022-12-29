'''
# import 
import 모듈
import 모듈 as 새이름
from 모듈 import 함수
from 모듈 import *

# exe 파일 생성
pyinstaller -w -F ./python/멜론차트100크롤링.py  <--- exe 파일로 생성
-w 는 cmd창 뜨지 않도록 하는 옵션
-F 는 exe 파일 하나로 만드는 옵션(단점. 실행시 압축풀고 실행하기에 느리다.)

#--onefile : 1개의 exe파일로 빌드
#--noconsole : 콘솔창 안보이게 빌드
pyinstaller --onefile --noconsole linw_v2.py

# PyQt 파일(.ui) 파이썬으로 컴파일(.py)
PyQt 파일(.ui) 컴파일 방법
pyuic5 -x ./변환할 파일이름.ui -o ./변환될 파일이름.py
#
'''

pyinstaller -w -F ./python/lineagetest.py