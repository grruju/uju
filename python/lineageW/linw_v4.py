from tkinter import *
from tkinter import messagebox, scrolledtext
import time, win32gui, cv2, sys
import numpy as np
import PIL.Image, PIL.ImageTk, PIL.ImageGrab
import webbrowser
import telepot
import autoit
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


class App:
    def __init__(self, window):
        self.window = window
        self.window.title("Lin W - Macro 2.0")
        self.window.resizable(width=False, height=False)
        self.window.geometry("+0+500")

        self.color_bg = "white"
        self.color_bg_active = "#2979FF"


        #Telegram part
        try:
            with open("C:/Users/river/GrrUJU/uju/python/lineageW/token.txt", "r") as f:
                self.telegram_bot = telepot.Bot(f.readline())
                self.telegram_bot.getMe()
                MessageLoop(self.telegram_bot, self.telegram_handle).run_as_thread()
                self.print_with_time("텔레그램이 연결되었습니다. 봇과 대화를 시작해 활성화 하세요.")
        except:
            self.print_with_time("token.txt파일을 찾을 수 없거나 올바른 토큰이 입력되지 않았습니다.")

        #frame_monitor
        self.frame_monitor = Frame(self.window)
        self.frame_monitor.pack()
        #frame_monitor = row 0
        self.win_label = Label(self.frame_monitor, text="Window")
        self.win_label.grid(row=0, column=0, padx=2, pady=2)

        self.win_hwnd = None
        self.win_list = []
        for win in self.win_get_list():
            if "리니지" in win[0]:
                self.win_list.append(win)
        if len(self.win_list) <= 0:
            messagebox.showinfo("Lin W not found", "게임 실행 후 사용해주세요.")
            #sys.exit()

        self.win_text = [list[0] for list in self.win_list]
        self.win_list_var = StringVar()
        self.win_list_var.set("")
        self.win_list_var.trace("w", self.evt_select)
        self.win = OptionMenu(self.frame_monitor, self.win_list_var, *self.win_text)
        self.win.config(width=22, anchor='w')
        self.win.grid(row=0, column=1, padx=2, pady=2)

        #frame_monitor = row 1
        self.hpp = Label(self.frame_monitor, text=" HP : ")
        self.hpp.grid(row=1, column=0, padx=2, pady=2)
        self.hp = Canvas(self.frame_monitor, width=190, height=12)
        self.hp.grid(row=1, column=1)
        
        #frame_monitor = row 2
        self.mpp = Label(self.frame_monitor, text=" MP : ")
        self.mpp.grid(row=2, column=0, padx=2, pady=2)
        self.mp = Canvas(self.frame_monitor, width=190, height=12)
        self.mp.grid(row=2, column=1)

        #frame 자동기능
        self.frame_auto = LabelFrame(self.window, text="자동기능")
        self.frame_auto.pack()
        self.home = self.make_toggle(self.frame_auto, "귀환")
        self.home.count = 0
        self.home_cool_state = False
        self.home.grid(row=0, column=0, padx=2, pady=2)
        self.tel = self.make_toggle(self.frame_auto, "순간이동")
        self.tel.grid(row=0, column=1, padx=2, pady=2)
        self.heal = self.make_toggle(self.frame_auto, "힐")
        self.heal.grid(row=0, column=2, padx=2, pady=2)
        self.setting = self.make_button(self.frame_auto, "설정", command=lambda: self.window_setting.deiconify())
        self.setting.grid(row=0, column=3, padx=2, pady=2)

        #Setting frame
        self.window_setting = Toplevel(self.window)
        self.window_setting.title("설정")
        self.window_setting.geometry("+280+500")
        self.window_setting.resizable(width=False, height=False)
        self.window_setting.protocol("WM_DELETE_WINDOW", lambda: self.window_setting.withdraw())
        self.window_setting.withdraw()

        #Setting frame - row 0
        self.frame_home = LabelFrame(self.window_setting, text="귀환")
        self.frame_home.grid(row=0, column=0, columnspan=4 , padx=2, pady=2)

        Label(self.frame_home, text="HP : ").grid(row=0, column=0, padx=2, pady=2)
        self.home_hp = Entry(self.frame_home, width=4)
        self.home_hp.insert(0, "40")
        self.home_hp.grid(row=0, column=1, padx=2, pady=2)
        Label(self.frame_home, text="Key : ").grid(row=0, column=2, padx=2, pady=2)
        self.home_key = Entry(self.frame_home, width=4)
        self.home_key.insert(0, "8")
        self.home_key.grid(row=0, column=3, padx=2, pady=2)
        self.home_repeat_state = BooleanVar()
        self.home_repeat = Checkbutton(self.frame_home, text="반복", width=11, var=self.home_repeat_state)
        self.home_repeat.grid(row=0, column=4, padx=2, pady=2)

        #Setting frame - row 1
        self.frame_tel = LabelFrame(self.window_setting, text="순간이동")
        self.frame_tel.grid(row=1, column=0, columnspan=4 , padx=2, pady=2)
        
        Label(self.frame_tel, text="HP : ").grid(row=0, column=0, padx=2, pady=2)
        self.tel_hp = Entry(self.frame_tel, width=4)
        self.tel_hp.insert(0, "60")
        self.tel_hp.grid(row=0, column=1, padx=2, pady=2)
        Label(self.frame_tel, text="Key : ").grid(row=0, column=2, padx=2, pady=2)
        self.tel_key = Entry(self.frame_tel, width=4)
        self.tel_key.insert(0, "7")
        self.tel_key.grid(row=0, column=3, padx=2, pady=2)
        Label(self.frame_tel, text="Cooltime : ").grid(row=0, column=4, padx=2, pady=2)
        self.tel_cool = Entry(self.frame_tel, width=4)
        self.tel_cool.insert(0, "3")
        self.tel_cool.grid(row=0, column=5, padx=3, pady=2)
        self.tel_cool_state = False

        #Setting frame - row 2
        self.frame_heal = LabelFrame(self.window_setting, text="힐")
        self.frame_heal.grid(row=2, column=0, columnspan=4 , padx=2, pady=2)
        
        Label(self.frame_heal, text="HP : ").grid(row=0, column=0, padx=2, pady=2)
        self.heal_hp = Entry(self.frame_heal, width=4)
        self.heal_hp.insert(0, "80")
        self.heal_hp.grid(row=0, column=1, padx=2, pady=2)
        Label(self.frame_heal, text="Key : ").grid(row=0, column=2, padx=2, pady=2)
        self.heal_key = Entry(self.frame_heal, width=4)
        self.heal_key.insert(0, "4")
        self.heal_key.grid(row=0, column=3, padx=2, pady=2)
        Label(self.frame_heal, text="Cooltime : ").grid(row=0, column=4, padx=2, pady=2)
        self.heal_cool = Entry(self.frame_heal, width=4)
        self.heal_cool.insert(0, "3")
        self.heal_cool.grid(row=0, column=5, padx=3, pady=2)
        self.heal_cool_state = False


        #frame 기타
        self.frame_etc = LabelFrame(self.window, text="기타")
        self.frame_etc.pack()
        self.hold = self.make_toggle(self.frame_etc , "고정사냥", command=lambda: self.print_with_time("아직 지원하지 않습니다."))
        self.hold.grid(row=0, column=0, padx=2, pady=2)
        self.inven = self.make_button(self.frame_etc , "가방", command=lambda: self.send_key(self.win_hwnd, "i"))
        self.inven.grid(row=0, column=1, padx=2, pady=2)
        telegram_noti = "텔레그램 활성화는 봇에게 채팅을 입력해 활성화 합니다."
        self.noti = self.make_button(self.frame_etc , "텔레그램", command=lambda: self.print_with_time(telegram_noti))
        self.noti.grid(row=0, column=2, padx=2, pady=2)
        self.noti.state = False
        self.youtube = self.make_button(self.frame_etc , "유튜브")
        self.youtube.grid(row=0, column=3, padx=2, pady=2)

        #frame 로그
        self.frame_log = LabelFrame(self.window, text="로그")
        self.frame_log.pack()
        self.log = scrolledtext.ScrolledText(self.frame_log, width=32, height=4, wrap=WORD)
        self.log.configure(state="disabled")
        self.log.pack()


        self.window.mainloop()

    def print_with_time(self, msg):
        now = time.localtime()
        text = "{}:{}:{} - {}".format(now.tm_hour, now.tm_min, now.tm_sec, msg)
        print(text)
        try:
            self.log.configure(state="normal")
            self.log.insert(END, text + "\n")
            self.log.yview(END)
            self.log.configure(state="disabled")
        except:
            pass


    def make_button(self, window, text, command=None):
        btn = Button(
            window,
            text=text,
            font="sans 10 bold",
            width=6,
            relief="groove",
            fg=self.color_bg_active,
            bg=self.color_bg,
            activeforeground=self.color_bg,
            activebackground=self.color_bg_active,
            command=command
        )
        return btn

    def make_toggle(self, window, text, command=None):       
        def on_click(e):
            btn.state = not btn.state
            btn["background"] = self.color_bg_active if btn.state else self.color_bg
            btn["foreground"] = self.color_bg if btn.state else self.color_bg_active

        btn = Button(
            window,
            text=text,
            font="sans 10 bold",
            width=6,
            relief="groove",
            fg=self.color_bg_active,
            bg=self.color_bg,
            activeforeground=self.color_bg,
            activebackground=self.color_bg_active,
            command=command
        )
        btn.state = False
        btn.bind("<Button-1>", on_click)
        return btn


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


    def send_key(self, hwnd, msg):
        win32gui.SetForegroundWindow(hwnd)
        self.print_with_time("Send key : {}".format(msg))
        if msg == "1":
            x, y = 53, 35
        elif msg == "2":
            x, y = 77, 35
        elif msg == "3":
            x, y = 99, 35
        elif msg == "4":
            x, y = 120, 35
        elif msg == "5":
            x, y = 142, 35
        elif msg == "6":
            x, y = 165, 35
        elif msg == "7":
            x, y = 185, 35
        elif msg == "8":
            x, y = 208, 35
        elif msg == "space":
            x, y = 160, 125
        elif msg == "i":
            x, y = 196, 59
        elif msg == "m":
            x, y = 190, 100

        try:
            if autoit.win_get_state("화상 키보드") == 7:
                autoit.control_click("화상 키보드", "[CLASS:DirectUIHWND]", x=x, y=y)
            else:
                self.print_with_time("ctrl+win+o 를 눌러화상키보드를 켜세요.")
        except:
            self.print_with_time("ctrl+win+o 를 눌러화상키보드를 켜세요.")


    def heal_cool_down(self):
        self.heal_cool_state = False


    def tel_cool_down(self):
        self.tel_cool_state = False

    def home_cool_down(self):
        self.home_cool_state = False


    def telegram_handle(self, msg):
        self.print_with_time("봇이 받은 메세지 : {}".format(msg["text"]))
        content_type, chat_type, self.telegram_room_id = telepot.glance(msg)
        self.telegram_bot.sendMessage(self.telegram_room_id, "Telegram notify start.")
        self.print_with_time("Telegram notify start.")
        self.noti.config(bg=self.color_bg_active, fg=self.color_bg)
        self.noti.state = True
        

    def update(self):
        if self.win_hwnd:
            try:
                x1, y1, x2, y2 = self.win_get_size(self.win_hwnd)
                #img_hp = self.win_get_image(x1 + 90, y1 + 31, x1 + 280, y1 + 40)
                img = self.win_get_image(x1 + 90, y1 + 29, x1 + 280, y1 + 53) #캡쳐 횟수를 1회로 변경 (기존 hp, mp 루프 당 1회씩)
                img_hp = img[0:11, 0:190] #캡쳐한 이미지를 잘라서 hp로 구분
                self.photo_hp = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img_hp))
                self.hp.create_image(0, 0, image = self.photo_hp, anchor = NW)
                hp_split = cv2.split(img_hp)[0] # hp바의 BGR색상 중 R값만 가져오기
                hp_blur = cv2.blur(hp_split, (5, 5)) # 블러 처리
                hp_thres = cv2.threshold(hp_blur, 222, 255, cv2.THRESH_BINARY)[1]  # 임계처리
                hp_point = np.flip(hp_thres).argmax()
                #hp바에서 가장 높은 값을 <- 방향으로 읽고, 백분율화
                hp_point = 100 if hp_point >= hp_thres.shape[1] else int((1-(np.flip(hp_thres).argmax()/hp_thres.shape[1])) * 100)  # 가끔 발생하는 초과값 수정 -200% 오류
                self.hpp.config(text="{}%".format(hp_point))


                #img_mp = self.win_get_image(x1 + 90, y1 + 45, x1 + 280, y1 + 53)
                img_mp = img[14:24, 0:190] #캡쳐한 이미지를 잘라서 mp로 구분
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

                #자동기능-귀환
                if self.home.state and not self.home_cool_state:
                    if hp_point <= int(self.home_hp.get()):
                        self.home.count += 1
                        if self.home.count >= 2: #2회 연속으로 발생 시
                            self.home.count = 0
                            cv2.imwrite("autohome.jpg", cv2.cvtColor(self.win_get_image(x1, y1, x2, y2), cv2.COLOR_RGB2BGR)) #귀환상황 캡쳐 추가
                            for i in range(3): #백업을 위해 3번 실행
                                self.send_key(self.win_hwnd, self.home_key.get())
                                time.sleep(0.3)


                            #텔레그램 연동옵션 추가
                            if self.noti.state:
                                #self.telegram_bot.sendMessage(self.telegram_room_id, "Auto home")
                                self.telegram_bot.sendPhoto(chat_id=self.telegram_room_id, photo=open("autohome.jpg", "rb"), caption="캐릭터가 귀환했습니다.") #귀환시 캡쳐 보내기

                            #귀환 반복 옵션
                            if self.home_repeat_state.get():
                                self.home_cool_state = True
                                self.window.after(10000, self.home_cool_down) #귀환 후 10초 뒤 재적용
                            
                            else:
                                self.home.state = False
                                self.home.config(fg=self.color_bg_active, bg=self.color_bg)

                            

                #자동기능-순간이동
                if self.tel.state:
                    if hp_point <= int(self.tel_hp.get()) and not self.tel_cool_state:
                        self.send_key(self.win_hwnd, self.tel_key.get())
                        self.tel_cool_state = True
                        self.window.after(int(self.tel_cool.get()) * 1000, self.tel_cool_down)


                #자동기능-힐
                if self.heal.state:
                    if hp_point <= int(self.heal_hp.get()) and mp_point >= 30 and not self.heal_cool_state:
                        self.send_key(self.win_hwnd, self.heal_key.get())
                        self.heal_cool_state = True
                        self.window.after(int(self.heal_cool.get()) * 1000, self.heal_cool_down)                


            except:
                #self.print_with_time("Screen capture failed")
                pass
                

        self.window.after(500, self.update)

App(Tk())