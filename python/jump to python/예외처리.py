# 오류 예외 처리 기법
'''
try:
    ...
except [발생 오류[as 오류 메세지 변수]]:
    ...
'''
# 1. try, except만 쓰는 방법
'''
try:
    ...
except:
    ...
'''

# 2. 발생 오류만 포함한 except문
'''
이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다.

try:
    ...
except 발생 오류:
    ...
'''

# 3. 발생 오류와 오류 메시지 변수까지 포함한 except문
'''
이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.

try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...
'''

# 예를 들면 다음과 같다.
try:
    4/0
except ZeroDivisionError as e:
    print(e)

# IndexError가 발생할 때 오류 메시지를 출력하는 소스를 작성해 보자.
a = [1,2]
try:
    a[3]
except IndexError as e:
    print(e)

# try ... finally
''' try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부와 상관없이 항상 수행된다.
보통 리소스를 close해야 할 때 많이 사용한다.
'''
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

print(say_nick("천사"))
print(say_nick("바보"))

