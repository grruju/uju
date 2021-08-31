# while 문의 기본 구조
'''
while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
    ...
'''

treeHit = 0             # <- 나무를 찍은 횟수
while treeHit < 10:     # <- 나무를 찍은 횟수가 10 미만인 경우 반복
    treeHit = treeHit + 1
    print("나무를 %s번 찍었습니다." % treeHit)
    if treeHit == 10:   # <- 나무를 열번 찍으면
        print("나무 넘어갑니다")

# while 문 만들기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0

while number !=4:
    print(prompt)
    number = int(input())
    if number !=4:
         pass
    else:
        print("정답")


# while문 강제로 빠져나가기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %s 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 커피 자판기
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1    
        print("남은 커피의 양은 %s 입니다." % coffee)
    elif money == 1000:
        break
    elif money > 300:
        print("거스름돈 %s를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1    
        print("남은 커피의 양은 %s 입니다." % coffee)
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")    
        print("남은 커피의 양은 %s 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break



# while 문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

# 연습문제. 1부터 10까지의 숫자 중에서 3의 배수를 뺸 나머지 값을 출력해 보자.
a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a)

# 무한루프
''' 무한루프 기본 문
while Ture:
    수행할 문장1
    수행할 문장2
    ...
'''
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
