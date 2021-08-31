a = 1
b = "python"
c = [1,2,3]

# 다른 프로그래밍 언어인 c나 java에서는 변수를 만들 때 자료형을 직접 지정해야 한다. 
# 하지만 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형을 지정하기 때문에 더 편하다.

a = [1,2,3]
print(id(a))  # id 함수는 변수가 가리키고 있는 객체의 주소 값을 돌려주는 파이썬 내장 함수이다.

b = a
print(id(b))

bool = a is b
print(bool)

a[1] = 4
print(a)
print(b)

# a, b 모두 동일한 리스트를 가르키기 때문에 동일 한 값 표시
# b 변수를 생성할 때 a 변수의 값을 가져오면서 a 와는 다른 주소를 가르키도록 만드는 방법은?

# 1. [:] 사용
a = [1,2,3]
b = a[:]    # 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1] = 4
print(a)
print(b)

# 2. copy 모듈 사용 - from copy import copy
from copy import copy   # 다음 단원에서 공부.. 일단 이거 없으면 오류 남.
a = [1,2,3]
b = copy(a)
a[1] = 4
print(a)
print(b)
print(b is a)

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print(a,b)
(a,b) = 'python', 'life'    # 튜플은 () 생략 가능
print(a,b)

[a,b] = ['python', 'life']  # 리스트로 변수 생성 가능
print([a,b])

# 여러 개의 변수에 같은 값을 대입할 수도 있다
a = b = 'python'
print(a)
print(b)

# 파이썬에서는 다음과 같은 방법으로 두 변수의 값을 바꿀 수 있다.
a = 3
b = 5
a,b = b,a   # a와 b의 값을 바꿈
print(a)
print(b)

# 다음 예제를 실행하고 그 결과를 설명해 보자.
a = [1,2,3]
b = [1,2,3]
a is b

print(id(a))
print(id(b))
print (a is b)  # a 와 b는 id 값이 다르기 때문에 False. copy 한다면 True 겠지...
c = a
print (c is a)

