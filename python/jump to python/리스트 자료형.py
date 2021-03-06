# 리스트 예시
odd = [1,3,5,7,9]
print(odd) # 결과값 [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트 인덱싱
a = [1,2,3]
print(a) # 결과값 [1, 2, 3]
print(a[0]) # 결과값 1
print(a[0:2]) # 결과값 [1, 2]
print(a[0] + a[2]) # 결과값 4(1+3)
print(a[-1]) # 결과값 3(-1은 리스트 끝부터)

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])     # 결과값 1
print(a[-1])    # 결과값 [1, 2, 3]
print(a[3][0])  # 결과값 a #마지막 리스트 값 [1, 2, 3] 을 가져온다음 그 리스트 안에서 다시 0번째 값 a 를 가져옴

# 삼중 리스트 인덱싱. 혼란스럽기 때문에 자주 쓰지 않는다.
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[-1][-1][0])

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
b = a[:2]   # 결과값 [1, 2]
c = a[2:]   # 결과값 [3, 4, 5]
print(b)
print(c)

d = a[1:3]
print(d)

# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5]) # 결과값 [3, ['a', 'b', 'c'], 4]
print(a[3][:2]) # 결과값 ['a', 'b']

# 리스트 연산하기
# 1. 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b) # 결과값 [1, 2, 3, 4, 5, 6]

# 2. 리스트 반복하기(*)
a = [1, 2, 3]
b = [4, 5, 6]
print(a*3) # 결과값 [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이 구하기
a = [1, 2, 3]
print(len(a))

# 테스트
a = [1, 2, 3]
# 원하는 값 3hi
print(str(a[2])+'hi')
b = a[2]
print(str(b)+'hi')

# 리스트의 수정과 삭제
a = [1, 2, 3]
a[2] = 4    # a 리스트의 2위치 값 3을 4로 변경. 변수 선언도 안하는데 어떻게 인식되는걸까...
print(a)

# del 함수 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1]
print(a)

# 슬라이싱 기법을 사용하여 리스트 요소 여러 개를 한꺼번에 삭제할 수 있다.
a = [1, 2, 3, 4, 5]
del a[2:] # 결과값 [1, 2]
print(a)