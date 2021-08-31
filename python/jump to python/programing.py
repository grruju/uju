# 구구단 만들기.
def GuGU(n):
    result = []         # <--- 결과값을 저장할 리스트 result
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result

print(GuGU(2))


# 3과 5의 배수 합하기
for n in range(1,1000):             # <--- 1부터 999까지 n에 대입하여 반복
    if n % 3 == 0 or n % 5 == 0:    # <--- n을 3으로 나눈 나머지가 0이거나 n을 5로 나눈 나머지가 0이라면
        print(n)


# 게시판 페이징 하기
def getTotalPage(m,n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1
print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))


# 간단한 메모장 만들기
