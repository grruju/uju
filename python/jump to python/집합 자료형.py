# 집합 자료형
s1 = set([1,2,3])
print(s1)

# set()의 괄호 안에 리스트를 입력하여 만들거나 다음과 같이 문자열을 입력하여 만들 수 있다.
s2 = set('Hello')
print(s2)

# 집합 자료형의 특징
'''
set('Hello') 의 결과가 이상하다.
Hello 문자열로 set 자료형을 만들었는데 생성된 자료형에는 l 문자가 빠져있고, 순서도 뒤죽박죽이다.
그 이유는 set 에 다음과 같은 2가지 큰 특징이 있기 때문이다. '''
# - 중복을 허용하지 않는다.
# - 순서가 없다(Unordered).
'''
리스트나 튜플은 순서가 있기(ordered) 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만 
set 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 값을 얻을 수 없다. '''
# 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후 해야 한다.
s1 = set([3,2,1])
print(s1)
l1 = list(s1)   # 리스트로 변환
print(l1)
print(l1[0])

t1 = tuple(s1)  # 튜플로 변환
print(t1)
print(t1[0])

# 교집합, 합집합, 차집합 - set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 - 기호: & , 함수: interseciton()
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 - 기호: | , 함수: union
print(s1 | s2)
print(s1.union(s2))

# 차집합 - 기호: - , 함수: difference 
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))


# 집합 자료형 관련 함수
# 값 1개 추가하기(add)
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러 개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)