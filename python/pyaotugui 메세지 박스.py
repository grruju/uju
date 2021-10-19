from typing import Text
import pyautogui

# 1.
btn1 = pyautogui.alert('경고','title','OKOK')
print(btn1)
print(type(btn1))


# 2.
btn2 = pyautogui.alert(text='경고',button='OJOJ',title='title')
print(btn1)

text = '경고'
title = '제목'
button = '확인'
btn3 = pyautogui.alert(text,title,button)

# 3.
btn3 = pyautogui.confirm(text='confirm test', title='Title', buttons=['1','2','3','4','5'])
if btn3 == 'OK':
    print('OK입니다.')
elif btn3 == 'Cancel':
    print('Cancle 입니다.')
else:
    print(button)

# 4.
btn4 = pyautogui.prompt(title='prompt 타이틀',default='여기에 쓰세요.',text='body')
print(btn4)

# 5.
btn5 = pyautogui.password('password','비밀번호를 입력하세요.',mask='$')
print(btn5)