import win32api
import win32con
import telepot
import autoit

## 커서 위치 확인하기
pos = win32api.GetCursorPos()
print(pos)
