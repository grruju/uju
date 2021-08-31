# 파일 생성하기
f = open("새파일.txt",'w')
f.close

# 파일 객채 = open(파일 이름, 파일 열기 모드)

'''
파일 열기 모드           설명
r                       읽기 모드 - 파일을 읽기만 할 때 사용
w                       쓰기 모드 - 파일에 내용을 쓸 때 사용
a                       추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
'''

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("c:/Users/river/Python/새파일.txt",'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)       # <--- f의 write 함수를 사용하여 파일에 결과값을 저장
f.close()


# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

# readline 함수 사용하기
f = open("c:/users/river/python/새파일.txt",'r')
line = f.readline()
print(line)
f.close()

# 위와 같이 실행하면 첫번쨰 라인만 출력된다. 모든 줄을 읽어서 출력하고자 한다면 다음과 같이 한다.
f = open("c:/users/river/python/새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 위 예제는 파일을 읽어서 출력하는 경우. 아래는 값을 받아서 출력하는 경우
while 1:
    data = input()
    if not data: break
    print(data)

# readlines 함수 사용하기
f = open("c:/users/river/python/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
'''
readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
따라서 위 예에서 lines는 리스트 ['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다.\n', 
'5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄입니다.\n', '9번째 줄입니다.\n', 
'10번째 줄입니다.\n'] 가 된다.
'''

# read 함수 사용하기
f = open("c:/users/river/python/새파일.txt",'r')
data = f.read()
print(data)
f.close()


# 파일에 새로운 내용 추가하기
f = open("c:/users/river/python/새파일.txt",'a')
for i in range(11, 20):     # <--- 11부터 19까지 i에 대입
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함꼐 사용하기
# close()를 사용하는 경우
f = open("foo.txt",'w')
f.write("life is too short, you need python")
f.close()

# with문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다.
with open("foo.txt",'w') as f:
    f.write("Life is too short, you need python")


# 파이썬에서는 sys 모듈을 사용하여 매개변수를 직접 줄 수 있다.
#sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)

# sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(),end=' ')
    