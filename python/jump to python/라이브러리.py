# TIME
import time

# time.time     UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수
print(time.time())

# time.localtime    time.time()이 돌려준 실수 값을 사용해서 연도,월,일,시,분,초 의 형태로 돌려준다
print(time.localtime())

# time.asctime      time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
print(time.asctime())

# time.ctime        asctime보다 간편하게 표시. 다른점은 항상 현재 시간만을 돌려준다.
print(time.ctime())

# time.strftime     시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# time.sleep        주로 루프 안에서 많이 사용된다. 일정한 시간 간격을 두고 루프를 실행할 수 있다.
import time
for i in range(10):
    print(i)
#    time.sleep(1)   # 1초 간격으로 0부터 9까지 숫자를 출력.


# calendar      파이썬에서 달력을 볼 수 있게 해주는 모듈
import calendar
print(calendar.calendar(2021))  # 그 해의 전체 달력을 보여준다.

print(calendar.prcal(2021))     # 위와 동일한결과값을 준다.

print(calendar.prmonth(2021, 8))    # 지정된 월의 달력만 보여준다.

print(calendar.weekday(2021,8,10))  # 그 날짜에 해당하는 요일을 돌려준다. 월요일0,화요일1,수요일2,목요일3,금요일4,토요일5,일요일6

print(calendar.monthrange(2021,8))  # 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지 튜플 형태로 보여준다.


# random    난수(규칙이 없는 임의의 수)를 발생시키는 모듈.
import random
print(random.random())          # 0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려줌
print(random.randint(1,10))     # 1에서 10 사이의 정수 중에서 난수 값을 돌려줌
print(random.randint(1,55))     # 1에서 55 사이의 정수 중에서 난수 값을 돌려줌


# webbrowser
import webbrowser
webbrowser.open("http://google.com")        # 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동한다.
webbrowser.open_new("http://google.com")    # 웹 브라우저가 실행된 상태라도 새로운 창으로 해당 주소가 열리게 한다.





