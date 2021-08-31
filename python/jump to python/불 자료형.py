''' 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다. 불 자료형은 다음 2가지 값만을 가질 수 있다.'''
# True : 참
# False : 거짓

a = True
b = False

print(a)
print(b)

print(type(a))
print(type(b))

print(1==1)
print(1==2)

print(2>1)
print(2<1)

# 참과 거짓이 프로그램에서 사용되는 예
a = [1,2,3,4]
while a:                # a가 참인동안
    print(a.pop())      # 리스트의 마지막 요소를 하나씩 꺼낸다.


# 불 연산 - bool 내장 함수를 사용하면 자료형의 참과 거짓을 식별할 수 있다.
a = bool('python')
print(a)

a = bool('')
print(a)
