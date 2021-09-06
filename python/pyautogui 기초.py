import pyautogui
import time

# pyautogui.position() -- 마우스 커서 위치 조회

# pyautogui.moveTo(30, 136, 2)

# pyautogui.click(clicks=2, interval=2)     # clicks = 2번 클릭, interval = 2초 뒤에 다시
# pyautogui.click(clicks=2)

pyautogui.moveTo(1666, 178, 2)

pyautogui.doubleClick()

time.sleep(1)   #time.sleep(1) 1초를 넣는 이유. 더블클릭을 통해 메모장이 열리는 와중에 Hello를 쓰기 위해 인터벌을 주기 위함.

pyautogui.typewrite('Hello')
pyautogui.typewrite(['Enter'])
pyautogui.typewrite('hahaha')

pyautogui.typewrite(['ENTER','a','b','c','enter','END'])    # 입력되는 키는 물리적으로 존재해야 한다.
