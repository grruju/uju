# key : value

# [Key1:Value1, Key2:Value2, Key3:Value3, ...]

dic = {'name:':'우주', 'phone':'01088962047', 'birth':'0130'}
print(dic)

a = {1:'hi'}
a = {'a':[1,2,3]}
print(a)

# 딕셔너리 추가
a = {1: 'a'}
a[2] = 'b'  # {2:'b'} 쌍 추가
print(a)    # 결과값 {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

# 딕셔너리 삭제
del a[1]
print(a)

# 딕셔너리 사용
{"김연아":"피겨스케이팅","류현진":"야구","박지성":"축구","우주":"파이썬"}

#딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

# 딕셔너리 만뜰 떄 주의사항
# Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시.
a = {1:'a', 1:'b', 1:'c', 1:'d'}
print(a)

# Key에서 리스트는 사용이 불가능하다. 튜플은 사용 가능하다.
a = {(1,2) : 'hi'}
print(a[(1,2)])

