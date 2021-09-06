import pyautogui

# pip install opencv-python # 별도 프로그램 설치 필요.
""" 
num7 = pyautogui.locateCenterOnScreen('python\img\calc7.png')

pyautogui.click(num7)

여기까지 기초.
"""

# 위의 예제는 계산기 숫자 7을 스크린샷으로 저장하여 비교하는 프로그램이다.
# 모든 계산기 버튼(프로그램)을 스크린샷으로 하기엔 너무 귀찮으니
# 프로그램 실행시 스크린샷을 찍어서 진행하는 예제로 해보겠다.


# print(pyautogui.position()) # 숫자 1의 포지션 1493, 864

pyautogui.screenshot('python\img\calc1.png', region=(1492, 850, 30, 30))    # 1493, 864 좌표의 30*30 스크린샷 찍음

num1 = pyautogui.locateCenterOnScreen('python\img\calc1.png')

pyautogui.screenshot('python\img\calc7.png', region=(1490, 627, 30, 30))    # 1493, 864 좌표의 30*30 스크린샷 찍음

num7 = pyautogui.locateCenterOnScreen('python\img\calc7.png')

pyautogui.click(num1)
pyautogui.click(num7)
pyautogui.click(num1)
pyautogui.click(num7)
pyautogui.click(num1)
pyautogui.click(num7)
pyautogui.click(num1)
pyautogui.click(num7)

# 단점. 스크린샷을 찍고 버튼을 클릭하는 과정이다보니 속도가 느림(약간의 딜레이).