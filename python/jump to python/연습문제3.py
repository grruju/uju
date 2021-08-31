# Q1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(number):
    if number % 2 == 1:     # 2로 나누었을 때 나머지가 1이면 홀수이다.
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))


# Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.(단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2))         #1.5 출력
print(avg_numbers(1,2,3,4,5))   #3.0 출력


# Q3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
input1 = input("첫번째 숫자를 입력하세요: ")
input2 = input("두번쨰 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다." % total)


# Q4. 다음 중 출력 결과가 다른 것 한 개를 골라 보자. 
# 3번
'''
1. print("you" "need" "python")
2. print("you" + "need" + "python")
3. print("you","need","python")                 # 콤마가 있는 경우 공백이 삽입되어 더해진다.
4. print("".join(["you","need","python"]))
'''


# Q5. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()                      # 열린 파일 객체를 닫는다.

f2 = open("test.txt",'r')
print(f2.read())


# Q6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt','a')
f.write(user_input)
f.write("\n")
f.close()


# Q7. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "Python"으로 바꾸어서 저장해 보자.
'''
Life is too short
you need java
'''

f = open('test4.txt', 'r')
body = f.read()
print(body)
f.close()

body = body.replace("java","python")

f = open('test4.txt','w')
f.write(body)
print(body)
f.close()