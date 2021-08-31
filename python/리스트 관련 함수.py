# 리스트에 요소 추가(append)
a =[1, 2, 3]
a.append(4) # a리스트에 4를 추가한다.
print(a) # 결과값 [1, 2, 3, 4]

# 리스트에 다시 리스트를 추가
a.append([5,6])
print(a) # 결과값 [1, 2, 3, 4, [5 , 6]]

# 리스트 정렬(sort)
a = [1, 4, 2, 5, 3, 6]
a.sort()
print(a)

b = ['a', 'd', 'c', 'b']
b.sort()
print(b)

# 리스트 뒤집기(reverse) - 그저 현재의 리스트를 그대로 거꾸로 뒤집는다.
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 위치 반환(index) - index(x) 함수는 리스트에 x 값이 있으면 x 의 값을 돌려준다.
z = [1, 2, 3, 'b']
print(z.index(3))   # 리스트에서 3을 찾아 자리 수 2 반환
print(z.index('b')) # 리스트에서 문자열 b를 검색하여 자리 수 3 반환

# 리스트에 요소 삽입(inset) - insert(a,b)는 리스트의 a번째 위치에 b를 삽입하는 함수.
a = [1, 2, 3]
a.insert(0, 4)
print(a) # [4, 1, 2, 3]
a.insert(3,5)
print(a) # [4, 1, 2, 5, 3]

# 리스트 요소 제거(remove) - remove(x) 리스트에 첫 번쨰로 나오는 x를 삭제하는 함수
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# 리스트 요소 끄집어내기(pop) - pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다
a = [1, 2, 3]
a.pop()
print(a)
# pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.
a = [1, 2, 3]
a.pop(1)
print(a)

# 리스트에 포함된 요소 x의 개수 세기(count) - count(x) 는 리스트 안에 x 가 몇개 있는지 조사하여 그 개수를 돌려주는 함수
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장(extend) - extend(x) 에서 x 에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b) # 변수인 b를 넣어도 계산 되네...
print(a)








