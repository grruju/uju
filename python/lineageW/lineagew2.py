import pyautogui
import time
import schedule
import random

def job():
    ### 마을 귀환 ###
    pyautogui.keyDown('F4')
    pyautogui.keyUp('F4')
    time.sleep(random.uniform(3,5))	# 2~4초 사이 랜덤한 시간으로 슬맆

    ### 말하는섬 마을 이동 ###
    pyautogui.keyDown('m')
    pyautogui.keyUp('m')
    time.sleep(random.uniform(3,5))	# 랜덤한 시간으로 슬맆
    pyautogui.moveTo(69, 188)       # 영지 메뉴 선택
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(135, 455)      # 말하는섬 선택
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(172, 533)      # 말하는섬 마을 선택
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(2321, 1311)      # 말하는섬 마을 이동
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(1363, 822)      # 텔레포트 확인 버튼 클릭
    pyautogui.click()
    
    ### 물약 재정비 ###
    time.sleep(random.uniform(3,5))	# 랜덤한 시간으로 슬맆
    pyautogui.moveTo(2295, 1106)   # 마을에서 검색 버튼 활성화
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(1453, 722)   # 상인 찾기
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(1538, 722)   # 잡화상인 찾기
    pyautogui.click()
    time.sleep(random.uniform(20,25))	# 랜덤한 시간으로 슬맆
    pyautogui.moveTo(2166, 1321)   # 자동구매품목 불러오기
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(2360, 1321)   # 모두 구매
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(2166, 1321)   # 자동구매품목 불러오기
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(2360, 1321)   # 모두 구매
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.keyDown('ESC')
    pyautogui.keyUp('ESC')
    time.sleep(random.uniform(1,2))


    ### 즐겨찾기 통해서 던전 진입 ###
    pyautogui.keyDown('m')
    pyautogui.keyUp('m')
    time.sleep(random.uniform(3,5))
    pyautogui.moveTo(61, 370)   # 즐겨찾기 아이콘 클릭
    pyautogui.click()
    time.sleep(random.uniform(2,3))
    pyautogui.moveTo(191, 459)   # 첫번째 즐겨찾기 클릭
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(2299, 1318)   # 텔레포트
    pyautogui.click()
    time.sleep(random.uniform(1,2))
    pyautogui.moveTo(1366, 823)   # 텔레포트
    pyautogui.click()

    # 잠시 휴식
    time.sleep(random.uniform(2,3))

    # 자사 시작
    pyautogui.moveTo(2369, 987)   # 어시스트 버튼 클릭
    pyautogui.click()
    # time.sleep(1)
    # pyautogui.keyDown('F2')          # 텔레포트
    # pyautogui.keyUp('F2')

    ### 사냥중 텔레포트 ###
# def teleport2():
#     pyautogui.keyDown('F2')
#     pyautogui.keyUp('F2')

# def one():
#     pyautogui.keyDown('1')
#     pyautogui.keyUp('1')


# x분에 한번씩 실행
schedule.every(100).minutes.do(job)
# schedule.every(9).minutes.do(teleport2)
# schedule.every(111).seconds.do(one)

'''
# 10초에 한번씩 실행
schedule.every(10).second.do(job)
# 매 시간 실행
schedule.every().hour.do(job)
# 매일 10:30 에 실행
schedule.every().day.at("10:30").do(job)
# 매주 월요일 실행
schedule.every().monday.do(job)
# 매주 수요일 13:15 에 실행
schedule.every().wednesday.at("13:15").do(job)
'''

while True:
    schedule.run_pending()
    time.sleep(1)



'''
    # ### 메뉴를 통해서 던전 진입 ###
    # pyautogui.moveTo(2438, 82)   # 메뉴 이동
    # pyautogui.click()
    # pyautogui.moveTo(2356, 330)   # 던전 이동
    # pyautogui.click()
    # pyautogui.moveTo(894, 163)   # 일반탭 선택
    # pyautogui.click()

    # 말하는섬
    # pyautogui.moveTo(195, 750, 1)   # 말하는섬던전 선택
    # pyautogui.click()
    # pyautogui.moveTo(1545, 484, 1)   # 1층 선택
    # pyautogui.click()
    # pyautogui.moveTo(1363, 824, 1)   # 확인
    # pyautogui.click()

    # 글루딘3층
    # pyautogui.moveTo(940, 746)   # 글루딘던전 선택
    # pyautogui.click()
    # pyautogui.moveTo(1547, 699)   # 3층 선택
    # pyautogui.click()
    # pyautogui.moveTo(1366, 825)   # 확인
    # pyautogui.click()

    # 개미굴1층
    # pyautogui.moveTo(1680, 741, 1)   # 개미굴 선택
    # pyautogui.click()
    # pyautogui.moveTo(1546, 590, 1)   # 1층2구역 선택
    # pyautogui.click()
    # pyautogui.moveTo(1363, 826, 1)   # 확인
    # pyautogui.click()
'''