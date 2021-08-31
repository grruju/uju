money = 2000
if money > 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if not card:
    print("빙고")
else:
    print("out")

pocket = ['paper', 'money', 'cellphone']
if 'card' not in pocket:
    print("걸어 가라")
else:
    print("버스를 타고 가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass                    # 조건문에서 아무 일도 하지 않게 설정하고 싶다면    pass    사용
else:
    print("카드를 꺼내라")

# 다양한 조건을 판단하는 elif
'''    주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라    '''
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라2")
    else:
        print("걸어 가라")

# elif 사용
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif 'paper' in pocket:
    print("택시를 타고 가라3")
elif card:
    print("택시를 타고 가라4")
else:
    print("걸어 가라")

# if문을 한 줄로 작성하기
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식
score = 50
if score >= 60:
    message = "success"
else:
    message = "failure"
''' 위 코드는  score가 60 이상일 경우 message에 문자열 "success"를, 아닐 경우 "failure"를 대입하는 코드이다
파이썬의 조건부 표현식(conditional expression)을 사용하면 위 코드를 다음과 같이 간단히 표현할 수 있다.'''
message = "success" if score >= 60 else "failure"
