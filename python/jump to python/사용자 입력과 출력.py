# input의 사용
a = input()     # input은 입력되는 모든 것을 문자열로 취급한다.
print(a)

# 프롬프트 값을 띄워서 사용자 입력받기
input("질문 내용")

number = input("숫자를 입력하세요: ")
print(number)

# print 자세히 알기

# 큰따옴표("")로 둘러싸인 문자열은 + 연산과 동일하다.
print("life" "is" "too short")
print("life"+"is"+"too short")

# 문자열 띄어쓰기는 콤마로 한다.
print("life", "is", "too short")

# 한 줄에 결과값 출력하기. 매개변수 end를 사용해 끝 문자 지정
for i in range(10):
    print(i, end=' ')

