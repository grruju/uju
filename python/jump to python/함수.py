# 파이썬 함수의 구조
'''
def 함수 이름(매개변수):
    수행할 문장1
    수행할 문장2
    ...
    return 결과값
'''
# 예
def add(a,b):   # <--- a,b는 매개변수. 함수에 입력으로 전달된 값을 받는 변수를 의미
    return a + b
''' 이 함수의 이름은 add이고 입력으로 2개의 값(a,b)을 받으며 결과값은 2개의 입력값을 더한 값이다.(a+b) '''

a = 3
b = 4
c = add(a, b)
print(c)

print(add(3,4)) # <--- 3,4는 인수. 함수를 호출 할 때 전달하는 입력값

# 일반 함수의 전형적인 예
def add(a,b):
    result = a + b
    return result

a = add(3,4)
print(a)

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

# 결과값이 없는 함수
def add(c,d):
    print("%d, %d의 합은 %d입니다." % (c, d, c+d))

print(add(3,4))

# 입력값도 결과값도 없는 함수
def say():
    print('Hi')

print(say())


# 매개변수 지정하여 호출하기
def add(a,b):
    return a+b

result = add(a=3, b=7) 
print(result)

# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.
result = add(b=5, a=3)
print(result)

# 입력값이 여러개인 경우
'''
def 함수이름(*매개변수):
    수행할 문장
    ...
'''

# 여러개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i     # *args에 입력받은 모든 값을 더한다.
    return result

result = add_many(1,2,3,4,5,6,7,8,9,10)

print(result)


def add_mul(choice, *args):
    if choice == "add":             # <--- 매개변수 choice에 'add'를 입력받았을 때
        result = 0
        for i in args:
            result = result + i     # <--- args에 입력받은 모든 값을 더한다.
    elif choice == "mul":           # <--- 매개변수 choice에 'mul'을 입력받았을 때
        result = 1
        for i in args:
            result = result * i     # <--- args에 입력받은 모든 값을 곱한다.
    return result

result = add_mul('add', 1,2,3,4,5)
print (result)

result = add_mul('mul', 1,2,3,4,5)
print (result)


# 키워드 파라미터
''' 키워드 파라미터를 사용할 떄는 매개변수 앞에 별 두개(**)를 붙인다. '''
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='foo', age=3)

# 함수의 결과값은 언제나 하나이다
def add_and_nul(a,b):
    return a+b, a*b

result = add_and_nul(1,3)
print(result)

# 만약 하나의 튜플 값을 2개의 결과값으로 받고 싶다면 다음과 같이 함수를 호출
result1, result2 = add_and_nul(1,3)
print(result1)
print(result2)

# return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)

'''
이 함수 역시 반환 값(결과값)은 없다. 문자열을 출력한다는 것과 반환 값이 있다는 것은 전혀 다른 일이다.
함수의 반환 값은 오로지 return문에 의해서만 생성된다.
'''
print(say_nick('야호'))
print(say_nick('바보'))

# 매개변수에 초기값 미리 설정하기
def say_myself(name, old, man=False):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man :
        print("남자입니다.")
    else:
        print("여자입니다.")

print(say_myself("강우주",34))
print(say_myself("강우주",34, True))

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)
''' 
함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 '함수만의 변수'이기 떄문에 결과값은 2가 아닌 1이 나온다.
def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수이지 함수 밖의 변수 a가 아니라는 뜻이다.
'''

# vartest_error.py
def vartest(a):
    a = a + 1

vartest(3)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
''' vartest라는 함수를 사용해서 함수 밖의 변수 a를 1만큼 증가시킬 수 있는 방법은 2가지. '''
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)  # vartest(a)의 결과값을 함수 밖의 변수 a에 대입
print(a)
'''
첫 번쨰 방법은 return을 사용하는 방법이다. vartest 함수는 입력으로 들어온 값에 1을 더한 값을 돌려준다.
따라서 a = vartest(a)라고 대입하면 a가 vartest 함수의 결과값으로 바뀐다.
'''

# global 명령어 사용하기
a = 2
def vartest():
    global a
    a = a + 1

vartest()
print(a)
''' global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다.
프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다. 왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다.
외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니므로, 첫번쨰 방법을 추천.
'''

# lambda
''' lamdba는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할.
보통 함수를 한줄로 간결하게 만들 때 사용.
def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는곳에 사용

lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식
'''
add = lambda a, b: a+b
result = add(3,4)
print(result)


