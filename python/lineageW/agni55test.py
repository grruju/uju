from tkinter import *
from tkinter import simpledialog, messagebox, ttk
import time, win32gui, cv2, pydirectinput, sys, webbrowser
import numpy as np
import PIL.Image, PIL.ImageTk, PIL.ImageGrab
###############################################################
import pyautogui
import time
import schedule
import random
from datetime import datetime


class App:
    def __init__(self, window):
        self.window = window
        self.window["bg"] = "white"
        self.window.title("agni W - 53")
        self.window.resizable(width=False, height=False)
        self.window.geometry("+0+0")

        self.bg_color = {"on" : "#4CAF50", "off" : "white"}
        self.fg_color = {"on" : "white", "off" : "black"}

        ################################################################################################
        self.win_label = Label(text="Window", bg=self.bg_color["off"])
        self.win_label.grid(row=0, column=0, padx=3, pady=2)
        self.win_hwnd = None
        self.win_list = []

        for win in self.win_get_list():
            if "리니지" in win[0]:
                self.win_list.append(win)
        if len(self.win_list) <= 0:
            messagebox.showinfo("Error", "게임 실행 후 사용해주세요.")
            sys.exit()

        self.win_text = [list[0] for list in self.win_list]
        self.win_list_var = StringVar()
        self.win_list_var.set("")
        self.win_list_var.trace("w", self.evt_select)
        self.win = OptionMenu(self.window, self.win_list_var, *self.win_text)
        self.win.config(width=22, anchor='w', bg=self.bg_color["off"])
        self.win.grid(row=0, column=1, columnspan=3, padx=3, pady=2)
        ################################################################################################
        self.hpp = Label(text=" HP : ", bg=self.bg_color["off"])
        self.hpp.grid(row=1, column=0, padx=3, pady=2)


        self.hp = Canvas(self.window, width=190, height=10, bg=self.bg_color["off"])
        self.hp.grid(row=1, column=1, columnspan=3)


        self.mpp = Label(text=" MP : ", bg=self.bg_color["off"])
        self.mpp.grid(row=2, column=0, padx=3, pady=2)


        self.mp = Canvas(self.window, width=190, height=10, bg=self.bg_color["off"])
        self.mp.grid(row=2, column=1, columnspan=3)
        ################################################################################################
        sep1 = ttk.Separator(self.window, orient="horizontal")
        sep1.grid(row=3, column=0, columnspan=4, sticky=NSEW)
        
        self.home = Button(self.window, text="Auto home", width=10, bg=self.bg_color["off"], relief="groove", command=self.btn_home)
        self.home.state = False
        self.home.count = 0
        self.home.grid(row=4, column=0, padx=3, pady=2)


        self.home_val = Button(self.window, text="20%", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_home_val)
        self.home_val.value = 20
        self.home_val.grid(row=4, column=1, padx=3, pady=2, sticky=NSEW)


        self.home_key = Button(self.window, text="key : F8", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_home_key)
        self.home_key.value = "F8"
        self.home_key.grid(row=4, column=2, padx=3, pady=2, sticky=NSEW)


        self.home_repeat = Button(self.window, text="Repeat", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_home_repeat)
        self.home_repeat.state = False
        self.home_repeat.grid(row=4, column=3, padx=3, pady=2, sticky=NSEW)
        ################################################################################################
        sep2 = ttk.Separator(self.window, orient="horizontal")
        sep2.grid(row=5, column=0, columnspan=4, sticky=NSEW)

        self.tel = Button(self.window, text="Auto tel", width=10, bg=self.bg_color["off"], relief="groove", command=self.btn_tel)
        self.tel.state = False
        self.tel.grid(row=6, column=0, padx=3, pady=2)


        self.tel_val = Button(self.window, text="40%", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_tel_val)
        self.tel_val.value = 40
        self.tel_val.grid(row=6, column=1, padx=3, pady=2, sticky=NSEW)


        self.tel_key = Button(self.window, text="key : F2", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_tel_key)
        self.tel_key.value = "F2"
        self.tel_key.grid(row=6, column=2, padx=3, pady=2, sticky=NSEW)


        self.tel_cool = Button(self.window, text="delay : 5s", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_tel_cool)
        self.tel_cool.value = 5
        self.tel_cool.state = False
        self.tel_cool.grid(row=6, column=3, padx=3, pady=2, sticky=NSEW)
        ################################################################################################
        sep3 = ttk.Separator(self.window, orient="horizontal")
        sep3.grid(row=7, column=0, columnspan=4, sticky=NSEW)

        self.heal = Button(self.window, text="Auto heal", width=10, bg=self.bg_color["off"], relief="groove", command=self.btn_heal)
        self.heal.state = False
        self.heal.grid(row=8, column=0, padx=3, pady=2)


        self.heal_val = Button(self.window, text="80%", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_heal_val)
        self.heal_val.value = 80
        self.heal_val.grid(row=8, column=1, padx=3, pady=2, sticky=NSEW)


        self.heal_key = Button(self.window, text="key : F1", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_heal_key)
        self.heal_key.value = "F1"
        self.heal_key.grid(row=8, column=2, padx=3, pady=2, sticky=NSEW)


        self.heal_cool = Button(self.window, text="delay : 3s", width=6, bg=self.bg_color["off"], relief="groove", command=self.btn_heal_cool)
        self.heal_cool.value = 3
        self.heal_cool.state = False
        self.heal_cool.grid(row=8, column=3, padx=3, pady=2, sticky=NSEW)
        ################################################################################################
        sep4 = ttk.Separator(self.window, orient="horizontal")
        sep4.grid(row=9, column=0, columnspan=4, sticky=NSEW)

        self.inven = Button(self.window, text="Inventory", width=10, bg=self.bg_color["off"], relief="groove", command=lambda:self.send_key(self.win_hwnd, "i"))
        self.inven.grid(row=10, column=0, padx=3, pady=2, sticky=NSEW)

        self.qna = Button(self.window, text="Q&A", width=6, bg=self.bg_color["off"], relief="groove", command=lambda:webbrowser.open("https://mandloh.tistory.com/70"))
        self.qna.grid(row=10, column=1, padx=3, pady=2,sticky=NSEW)

        self.youtube = Button(self.window, text="테스트", width=6, bg=self.bg_color["off"], relief="groove", command=self.job)
        self.youtube.grid(row=10, column=2, columnspan=2 , padx=3, pady=2, sticky=NSEW)


        self.window.mainloop()


    def print_with_time(self, msg):
        now = time.localtime()
        print("{}/{}/{} {}:{}:{} - {}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec, msg))


    def update(self):
        if self.win_hwnd:
            try:
                x1, y1, x2, y2 = self.win_get_size(self.win_hwnd)
                img_hp = self.win_get_image(x1 + 90, y1 + 28, x1 + 280, y1 + 40)          # 1280*720 해상도 버전
                self.photo_hp = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img_hp))
                self.hp.create_image(0, 0, image = self.photo_hp, anchor = NW)
                hp_split = cv2.split(img_hp)[0] # hp바의 BGR색상 중 R값만 가져오기
                hp_blur = cv2.blur(hp_split, (5, 5)) # 블러 처리
                hp_thres = cv2.threshold(hp_blur, 222, 255, cv2.THRESH_BINARY)[1]  # 임계처리
                hp_point = np.flip(hp_thres).argmax()
                #hp바에서 가장 높은 값을 <- 방향으로 읽고, 백분율화
                hp_point = 100 if hp_point >= hp_thres.shape[1] else int((1-(np.flip(hp_thres).argmax()/hp_thres.shape[1])) * 100)  # 가끔 발생하는 초과값 수정 -200% 오류
                self.hpp.config(text="{}%".format(hp_point))


                img_mp = self.win_get_image(x1 + 90, y1 + 43, x1 + 280, y1 + 53)
                self.photo_mp = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img_mp))
                self.mp.create_image(0, 0, image = self.photo_mp, anchor = NW)
                img_mp = cv2.cvtColor(img_mp, cv2.COLOR_RGB2HSV)
                blueLower = (120-30, 30, 30)
                blueUpper = (120-10, 255, 255)
                img_mp = cv2.inRange(img_mp, blueLower, blueUpper)
                img_mp = cv2.blur(img_mp, (3,3))
                img_mp = cv2.threshold(img_mp, 170, 255, cv2.THRESH_BINARY)[1] #임계처리
                mp_point = int((1-(np.flip(img_mp).argmax()/img_mp.shape[1])) * 100)
                self.mpp.config(text="{}%".format(mp_point))


                #Auto home part
                if self.home.state:
                    if hp_point <= self.home_val.value:
                        self.home.count += 1
                        if self.home.count >= 2: #2회 연속으로 발생 시
                            self.home.count = 0
                            for i in range(3): #백업을 위해 여러번 실행
                                # self.send_key(self.win_hwnd, self.home_key.value)             # 기존 숫자패드 입력을 pyautogui로 변경
                                pyautogui.keyDown(self.home_key.value)
                                pyautogui.keyUp(self.home_key.value)
                                time.sleep(0.3)
                                print(self.home_key.value)
                            
                            self.home.state = False
                            self.home.config(bg=self.bg_color["off"], fg=self.fg_color["off"])
                            
                            if self.home_repeat.state: #반복옵션 5초후 다시 켜기
                                self.window.after(5000, self.auto_home_repeat)
                            else:
                                self.tel.state = False
                                self.tel.config(bg=self.bg_color["off"], fg=self.fg_color["off"])
                                self.heal.state = False
                                self.heal.config(bg=self.bg_color["off"], fg=self.fg_color["off"])
                        self.job()

                #Auto tel part
                if self.tel.state:
                    if hp_point <= self.tel_val.value and not self.tel_cool.state:
                        # self.send_key(self.win_hwnd, self.tel_key.value)          # 기존 숫자패드 입력을 pyautogui로 변경
                        for i in range(2): #백업을 위해 여러번 실행
                            pyautogui.keyDown(self.tel_key.value)
                            pyautogui.keyUp(self.tel_key.value)
                            time.sleep(0.3)
                        self.tel_cool.state = True
                        self.window.after(self.tel_cool.value * 1000, self.auto_tel_cool)


                #Auto heal part
                if self.heal.state:
                    if hp_point <= self.heal_val.value and mp_point >= 30 and not self.heal_cool.state:
                        # self.send_key(self.win_hwnd, self.heal_key.value)          # 기존 숫자패드 입력을 pyautogui로 변경
                        pyautogui.keyDown(self.heal_key.value)
                        pyautogui.keyUp(self.heal_key.value)
                        self.heal_cool.state = True
                        self.window.after(self.heal_cool.value * 1000, self.auto_heal_cool)
            
            except:
                print("Screen capture failed")


        self.window.after(500, self.update)


    def win_get_list(self):
        def callback(hwnd, hwnd_list: list):
            title = win32gui.GetWindowText(hwnd)
            if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
                hwnd_list.append((title, hwnd))
            return True
        output = []
        win32gui.EnumWindows(callback, output)
        return output


    def win_get_size(self, hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        return left, top, right, bottom


    def win_get_image(self, x1, y1, x2, y2):
        img = np.array(PIL.ImageGrab.grab(bbox=(x1, y1, x2, y2)))
        return img
        

    def evt_select(self, *args):
        for list in self.win_list:
            if self.win_list_var.get() in list:
                self.win_hwnd = list[1]
                self.print_with_time("Window : {}".format(list))
                self.update() #start sub loop


    def auto_home_repeat(self):
        if self.home_repeat.state:
            self.home.state = True
            self.home.config(bg=self.bg_color["on"], fg=self.fg_color["on"])


    def auto_heal_cool(self):
        self.heal_cool.state = False


    def auto_tel_cool(self):
        self.tel_cool.state = False
            
            
    def send_key(self, hwnd, msg):
        win32gui.SetForegroundWindow(hwnd)
        pydirectinput.write(msg)
        self.print_with_time("Send key : {}".format(msg))


    def btn_home(self):
        self.home.state = not self.home.state
        self.home.config(bg=self.bg_color["on"] if self.home.state else self.bg_color["off"], fg=self.fg_color["on"] if self.home.state else self.fg_color["off"])
        self.print_with_time("Auto home : {}".format(self.home.state))


    def btn_tel(self):
        self.tel.state = not self.tel.state
        self.tel.config(bg=self.bg_color["on"] if self.tel.state else self.bg_color["off"], fg=self.fg_color["on"] if self.tel.state else self.fg_color["off"])
        self.print_with_time("Auto tel : {}".format(self.tel.state))


    def btn_heal(self):
        self.heal.state = not self.heal.state
        self.heal.config(bg=self.bg_color["on"] if self.heal.state else self.bg_color["off"], fg=self.fg_color["on"] if self.heal.state else self.fg_color["off"])
        self.print_with_time("Auto heal : {}".format(self.heal.state))


    def btn_home_val(self):
        input = int(simpledialog.askstring(title="Set value", prompt="Type number"))
        self.home_val.config(text="{}%".format(input))
        self.home_val.value = input
        self.print_with_time("Auto home value : {}".format(self.home_val.value))
        

    def btn_tel_val(self):
        input = int(simpledialog.askstring(title="Set value", prompt="Type number"))
        self.tel_val.config(text="{}%".format(input))
        self.tel_val.value = input
        self.print_with_time("Auto tel value : {}".format(self.tel_val.value))


    def btn_heal_val(self):
        input = int(simpledialog.askstring(title="Set value", prompt="Type number"))
        self.heal_val.config(text="{}%".format(input))
        self.heal_val.value = input
        self.print_with_time("Auto heal value : {}".format(self.heal_val.value))


    def btn_home_key(self):
        input = simpledialog.askstring(title="Set value", prompt="Type key")
        self.home_key.config(text="key : "+input)
        self.home_key.value = input


    def btn_tel_key(self):
        input = simpledialog.askstring(title="Set value", prompt="Type key")
        self.tel_key.config(text="key : "+input)
        self.tel_key.value = input


    def btn_heal_key(self):
        input = simpledialog.askstring(title="Set value", prompt="Type key")
        self.heal_key.config(text="key : "+input)
        self.heal_key.value = input


    def btn_home_repeat(self):
        self.home_repeat.state = not self.home_repeat.state
        self.home_repeat.config(bg=self.bg_color["on"] if self.home_repeat.state else self.bg_color["off"], fg=self.fg_color["on"] if self.home_repeat.state else self.fg_color["off"])
        self.print_with_time("Auto home repeat : {}".format(self.home_repeat.state))


    def btn_tel_cool(self):
        input = int(simpledialog.askstring(title="Set value", prompt="Type number"))
        self.tel_cool.config(text="delay : {}s".format(input))
        self.tel_cool.value = input


    def btn_heal_cool(self):
        input = int(simpledialog.askstring(title="Set value", prompt="Type number"))
        self.heal_cool.config(text="delay : {}s".format(input))
        self.heal_cool.value = input
    
    def job(self):
        ### 마을 귀환 ###
        pyautogui.moveTo(640, 432)       # 화면 선택
        pyautogui.click()
        pyautogui.keyDown('F4')
        pyautogui.keyUp('F4')
        now = time.localtime()
        print("{}/{}/{} {}:{}:{} - {}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec, '귀환'))
        time.sleep(random.uniform(5,5))	# 2~5초 사이 랜덤한 시간으로 슬맆

        # ## 말하는섬 마을 이동 ###
        # pyautogui.keyDown('m')
        # pyautogui.keyUp('m')
        # time.sleep(random.uniform(2,3))	# 랜덤한 시간으로 슬맆
        # pyautogui.moveTo(40, 130)       # 영지 메뉴 선택
        # pyautogui.click()
        # time.sleep(random.uniform(1,2))
        # pyautogui.moveTo(81, 296)      # 말하는섬 선택
        # pyautogui.click()
        # time.sleep(random.uniform(1,2))
        # pyautogui.moveTo(103, 344)      # 말하는섬 마을 선택
        # pyautogui.click()
        # time.sleep(random.uniform(1,2))
        # pyautogui.moveTo(1125, 708)      # 말하는섬 마을 이동
        # pyautogui.click()
        # time.sleep(random.uniform(1,2))
        # pyautogui.moveTo(708, 462)      # 텔레포트 확인 버튼 클릭
        # pyautogui.click()
        
        # ## 물약 재정비 ###
        # time.sleep(random.uniform(3,5))	# 랜덤한 시간으로 슬맆
        pyautogui.moveTo(1150, 577)   # 마을에서 검색 버튼 활성화
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.moveTo(762, 399)   # 상인 찾기
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.moveTo(816, 399)   # 잡화상인 찾기
        pyautogui.click()
        time.sleep(random.uniform(12,12))	# 랜덤한 시간으로 슬맆
        pyautogui.moveTo(1061, 709)   # 자동구매품목 불러오기
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.moveTo(1187, 707)   # 모두 구매
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.moveTo(1046, 707)   # 자동구매품목 불러오기
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.moveTo(1207, 708)   # 모두 구매
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.keyDown('ESC')
        pyautogui.keyUp('ESC')
        time.sleep(random.uniform(1,2))

        time.sleep(random.uniform(5,7))	# 2~4초 사이 랜덤한 시간으로 슬맆

        ### 즐겨찾기 통해서 던전 진입 ###
        pyautogui.keyDown('m')
        pyautogui.keyUp('m')
        time.sleep(random.uniform(3,5))
        pyautogui.moveTo(35, 243)   # 즐겨찾기 아이콘 클릭
        pyautogui.click()
        time.sleep(random.uniform(2,3))
        pyautogui.moveTo(104, 296)   # 첫번째 즐겨찾기 클릭
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.moveTo(1127, 711)   # 텔레포트
        pyautogui.click()
        time.sleep(random.uniform(1,2))
        pyautogui.moveTo(705, 461)   # 텔레포트
        pyautogui.click()

        # 잠시 휴식
        # time.sleep(random.uniform(2,3))
        time.sleep(2)

        # 자사 시작
        pyautogui.moveTo(1194, 502)   # 어시스트 버튼 클릭
        pyautogui.click()
        pyautogui.moveTo(640, 354)

        time.sleep(1)
        pyautogui.keyDown('F2')          # 텔레포트
        pyautogui.keyUp('F2')
App(Tk())