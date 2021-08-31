# 튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
# 리스트는 []으로 둘러싸이지만 튜플은()으로 둘러싼다.
# 리스트는 그 값의 생성,삭제,수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# t2 = (1,) 처럼 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다.
# t4 = 1, 2, 3 처럼 괄호()를 생략해도 무방하다.

# 튜플 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])    # 결과값 1
print(t1[3])    # 결과값 'b'

# 튜플 슬라이싱
print(t1[1:])   # 결과값 (2, 'a', 'b')

# 튜플 더하기
t2 = (3, 4)
print(t1 + t2)  # 결과값 (1, 2, 'a', 'b', 3, 4)

# 튜플 곱하기
print(t2 * 3)   # 결과값 (3, 4, 3, 4, 3, 4)

# 튜플 길이 구하기
print(len(t1))  # 결과값 4

'''(1,2,3)이라는 튜플에 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.'''
z1 = (1, 2, 3)
print(z1+(4,))
