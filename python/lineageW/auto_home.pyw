import win32gui
import serial
import serial.tools.list_ports as sp
import PySimpleGUI as sg
from PIL import ImageGrab
import cv2
import numpy as np
import time

#기준 해상도 1280x720
win_hwnd = None
ser = False
auto_home = False
auto_home_point = 40  # 귀환하는 HP 비율
auto_home_count = 0
auto_home_count_max = 2  # 가끔 발생하는 검은화면을 인식해 귀환하는 오류방지용


def getWinList():
    def callback(hwnd, hwnd_list: list):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
            hwnd_list.append((title, hwnd))
        return True
    output = []
    win32gui.EnumWindows(callback, output)
    return output


def getWinSize(hwnd):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    return left, top, right, bot


def setForeground(hwnd):
    win32gui.SetForegroundWindow(hwnd)


def getImage(x1, y1, x2, y2):
    img = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2))), cv2.COLOR_BGR2RGB)
    return img


def sendKey(msg):
    setForeground(win_hwnd)
    ser.write(msg.encode())


win_list = getWinList()
win_text = [list[0] for list in win_list]

com_list = [i.device for i in sp.comports()]
com_port = None

col = [
    [sg.Text("Win", size=(5,1)), sg.Combo(values=win_text, key="WIN", size=(20,1), readonly=True)],
    [sg.Text("Com", size=(5,1)), sg.Combo(values=com_list, key="COM", size=(20,1), readonly=True)],
]

lay = [
    [sg.Col(col), sg.Button("App start", key="START", expand_x=True, expand_y=True), sg.Button("Check", key="BAG", expand_x=True, expand_y=True)],
    [sg.Text("00%", key="HP"), sg.Image(filename="", size=(190, 20), key="HPIMG"), sg.Text("ON"),
        sg.Slider(range=(1, 0), size=(5, 25), default_value=0, key="TOGGLE_AUTOHOME", enable_events=True, disable_number_display=True, orientation="h"),
        sg.Text("OFF")],
]


window = sg.Window("LineageW", lay, location=(1300, 0))

while True:
    event, values = window.read(timeout=400)

    if event in ("Exit", None):
        break

    elif event == "START":
        try:
            win_hwnd = win_list[win_text.index(values["WIN"])][1]
            print("hwnd : {}".format(win_hwnd))
        except:
            print("Window handle error.")
        com_port = values["COM"]
        if ser:
            ser.close()
        try:
            ser = serial.Serial(port=com_port, baudrate=9600)
            print("Serial is connected at {}.".format(com_port))
        except:
            print("Serial connection error.")
            ser = None

    elif event == "BAG":
        if ser and win_hwnd:
            sendKey('i')
        else:
            print("Window handle, Serial needed.")

    elif event == "TOGGLE_AUTOHOME":
        auto_home = True if values["TOGGLE_AUTOHOME"] else False

    if win_hwnd:
        try:
            x1, y1, x2, y2 = getWinSize(win_hwnd)
            hp = getImage(x1 + 90, y1 + 30, x1 + 280, y1 + 40)
            window["HPIMG"].update(data=cv2.imencode(".png", hp)[1].tobytes())
            hp_split = cv2.split(hp)[2] # hp바의 BGR색상 중 R값만 가져오기
            hp_blur = cv2.blur(hp_split, (5, 5)) # 블러 처리
            hp_thres = cv2.threshold(hp_blur, 222, 255, cv2.THRESH_BINARY)[1]  # 임계처리
            hp_point = np.flip(hp_thres).argmax()
            #hp_point = int((1-(np.flip(hp).argmax()/hp.shape[1])) * 100) #hp바에서 가장 높은 값을 <- 방향으로 읽고, 백분율화
            hp_point = 100 if hp_point >= hp_thres.shape[1] else int((1-(np.flip(hp_thres).argmax()/hp_thres.shape[1])) * 100)  # 가끔 발생하는 초과값 수정 -200% 오류
            window["HP"].update("{}%".format(hp_point))
            

            #Automation part
            if auto_home:
                if hp_point <= auto_home_point:
                    auto_home_count += 1
                    if auto_home_count >= auto_home_count_max:
                        auto_home_count = 0
                        sendKey("8")
                        print("HOME")
                        auto_home = False
                        window["TOGGLE_AUTOHOME"].update(value=0)
                        print("Auto Home")
                        time.sleep(0.5)
                        sendKey("8")  # backup
                else:
                    auto_home_count = 0

        except:
            print("Screen capture failed.")


if ser:
    ser.close()
window.close()
