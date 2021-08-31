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

# 포매팅 연산자 %d 와 %를 같이 쓰는 경우
a = "Error is %d%%." % 98
print(a)


# 포맷 코드와 숫자 함께 사용

# 정렬과 공백
a = "%10s" % "hi"
print(a)

b = "%-10sjane%10s" % ('hi','bye')
print(b)

c = "%10.4f" % 3.42134234
print(c)



# format  함수
#숫자 바로 대입
a = 'I eat {0} apples'.format(3)
print(a)

#문자열 바로 대입
b = 'i eat {0} apples.'.format("five")
print(b)

#변수 대입
number = 3
c = 'I eat {0} apples.'.format(number)
print(c)

#2개 이상의 값
number = 10
day = "three"
d = "I eat {0} apples. so I was sick for {1} days.".format(number,day)
print(d)

#이름으로 넣기
e = "I eat {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(e)

#인덱스와 이름을 혼용
f = "I eat {0} apples. so I was sick for {day} days.".format(10, day=3)
print(f)

#왼쪽 정렬
g = "{0:<10}".format("hi")
print(g)

#오른쪽 정렬
h = "{0:>10}".format("hi")
print(h)

# 가운데 정렬
i = "{0:^10}".format("hi")
print(i)

# 공백채우기
j = "{0:=^10}".format("hi")
print(j)
j = "{0:!<10}".format("hi")
print(j)

# 소수점 표현
y = 3.42134234
k = "{0:0.4f}".format(y)
print(k)
k = "{0:10.4f}".format(y)
print(k)
