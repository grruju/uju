# for 문의 기본 구조
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
'''

# 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한 for 문의 사용
a = [(1,2), (4,5), (7,8)]
for (first, last) in a:
    print(first + last)

# for 문의 응용
''' 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 
그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.'''
marks = [90, 25, 67, 45, 80]
number = 0
for i in marks:
    number = number + 1
    if i > 60:
        print("%s번 학생은 %s점으로 합격입니다." % (number, i))
    else:
        print("%s번 학생은 %s점으로 불합격입니다." %(number,i))

# for 문과 continue 문
marks = [90, 25, 67, 45, 80]
number = 0
for i in marks:
    number = number + 1
    if i < 60: continue
    print("%s번 학생 축하합니다. %s점으로 합격입니다." % (number, i))

# for 문과 함께 자주 사용하는 range 함수
''' for 문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함꼐 사용하는 경우가 많다
다음은 range 함수의 간단한 사용법이다.'''
a = range(10)
print(a)
a = range(1,11)     # 시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 사용 이때 끝 숫자는 포함되지 않는다.

# range 함수의 예시
add = 0
for i in range(1, 11):
    add = add + i
    print(add)

# '60점 이상이면 합격' 이라는 문장을 출력하는 예제도 range 함수를 사용해서 바꿀 수 있다.
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue     # <- 점수가 60점 미만이면 맨 처음으로 돌아간다.
    print("%s번 학생 축하합니다. %s점 합격입니다." % (number+1,marks[number]))


# for 문과 range 함수를 사용하여 1부터 100까지 더해 보자.
a = 0
for i in range(1,101):
    a += i
    if i == 100:
        print(a)

# for와 range를 사용한 구구단
for i in range(1,10):
    for j in range(1, 10):
        print(i*j, end=" ") # 매개변수 end를 넣어 준 이유는 해당 결과값을 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속해서 출력
        print('')


# 리스트 내포 사용하기
''' 리스트 안에 for문을 포함하는 리스트 내포(List comprehension)를 사용하면 좀더 편하고 직관적인 프로그램 만들 수 있다. '''
# 예제
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)   # 결과값 [3,6,9,12]

# 리스트 내포 사용
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

# 만약 [1,2,3,4] 중에서 짝수에만 3을 곱하여 담고 싶다면 리스트 내포 안에 if 조건을 사용할 수 있다.
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 리스트 내포 일반 문법
'''
[포현식 for 항목 in 반복 가능 객체 if 조건]
'''

# for문 2개 이상 사용
'''
[표현식 for 항목1 in 반복 가능 객체1 if 조건1
        for 항목2 in 반복 가능 객체2 if 조건2
        ...
        for 항목n in 반복 가능 객체n if 조건n]
'''

# 만약 구구단의 모든 결과를 리스트에 담고 싶다면
result = [x*y for x in range(1,10)
        for y in range(1,10)]
print(result)