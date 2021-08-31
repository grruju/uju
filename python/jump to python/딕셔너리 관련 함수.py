dic = {'name:':'우주', 'phone':'01088962047', 'birth':'0130'}
# dict_keys, dict_values, dict_items
print(dic.keys())       #결과값 dict_keys(['name:', 'phone', 'birth'])
print(dic.values())     #결과값 dict_values(['우주', '01088962047', '0130'])
print(dic.items())      #결과값 dict_items([('name:', '우주'), ('phone', '01088962047'), ('birth', '0130')])

print(list(dic.keys())) # 파이썬 2.7버전까지는 list로 반환했었음. list로 받고자 하면 사용

# Key, Value 쌍 얻기(items)
print(dic.items())      #item 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.

# Key: Value 쌍 모두 지우기(clear)
dic.clear()
print(dic)

''' 비어 있는 딕셔너리는 dic = dict()로 생성할 수 있다. '''
dic = dict([('name:', '우주'), ('phone', '01088962047'), ('birth', '0130')])
print(dic.keys()) 
print(dic.values())
print(dic.items())

# Key로 Value 얻기(get)
a = {'name':'우주', 'phone':'01088962047', 'birth':'0130'}
print(a.get('name'))
print(a['name'])
'''
get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다. a.get('name')은 a['name']과 같다.
다만, 다음 예제에서 볼 수 있듯이 a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고 할 경우 a['nokey']는 Key 오류를 발생시키고 
a.get('nokey')는 None을 돌려준다는 차이가 있다.
'''
# 예제
print(a.get('nokey'))
# print(a.['nokey']) <--- SyntaxError: invalid syntax


# 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때
# get(x,'디폴트값') 을 사용한다.
print(a.get('nokey','bar')) # a 딕셔너리에는 'nokey'에 해당하는 값이 없다. 따라서 디폴트 값인 'bar'를 돌려준다.


# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'우주', 'phone':'01088962047', 'birth':'0130'}
print('name' in a)
print('email' in a)
'''
'name' 문자열은 a 딕셔너리의 Key 중 하나이다. 따라서 'name' in a 를 호출하면 참(True)을 돌려준다.
반대로 'email'은 a 딕셔너리 안에 존재하지 않는 Key이므로 거짓(False)를 돌려준다
'''

# 다음 표를 딕셔너리로 만드시오.
'''
항목    값
name    홍길동
birth   1128
age     30
'''
a = {'name':'홍길동', 'birth': '1128', 'age': '30'}
print(a)