# 숫자 바로 대입
a = "I eat %d apples." % 3
print(a)

# 문자열 바로 대입
a = "I eat %s apples." % "five"
print(a)

# 숫자 값을 나타내는 변수로 대입
number = 3
a = "I eat %d apples." % number
print(a)

# 2개 이상의 값 넣기
number = 10
day = "three"
a = "I eat %d apples. so I was sick for %s days." % (number, day)
print(a)


"""
# 문자열 포맷 코드
    %s      문자열(String)
    %c      문자1개(Character)
    %d      정수(Integer)
    %f      부동 소수(Floating-point)
    %o      8진수
    %x      16진수
    %%      Literal % (문자 '%' 자체)

"""

# 예제
# % 기호 문자 출력
names = ["kim", "park", "lee"]
for name in names :
        print("my name is %s" % name)

# % 기호 정수 출력
money = 10000
s2 = 'give me %d won' % money
print(s2)

# % 기호 실수 출력
d = 3.141592
print('value %f' % d)

# 포매팅 변수 2개 이상일 경우
s1 = 'my name is %s. age : %d' % ('kang woo ju', 100)
print(s1)