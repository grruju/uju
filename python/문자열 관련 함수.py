# 변수 이름 뒤에 . 를 붙인 다음 함수 이름 사용
a = "hobby"
print(a.count('b')) # 결과 2

# 위치 알려주기 1(find)
a = "Python is the best choice"
print(a.find('b')) # 결과값 14
print(a.find('k')) # 결과값 -1 . 찾는 값이 존재하지 않는다면 -1을 반환.

# 위치 알려주기 2(index)
a = "Life is too short"
print(a.index('t')) # 결과값 8
# print(a.index('k')) # k가 없기 떄문에 오류 발생

# 문자열 삽입(join)
print(",".join('abcd')) # 결과값 a,b,c,d
print(",".join(['a','b','c','d'])) # 결과값 a,b,c,d # join 함수의 입력으로 리스트를 사용하는 예

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper()) # 결과값 HI

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
print(a.lower()) # 결과값 hi

# 왼쪽 공백 지우기(lstrip)
a = "hi "
print(a.lstrip()) # 결과값 'hi '

# 오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip()) # 결과값 ' hi'

# 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip()) # 결과값 'hi'

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg")) # 결과값 Your leg is too short

# 문자열 나누기(split)
a = "Life is too short"
print(a.split()) # 결과값 ['Life', 'is', 'too', 'short'] # 공백을 기준으로 문자열을 나눔
b = "a:b:c:d"
print(b.split(":")) # 결과값 ['a', 'b', 'c', 'd'] # 기호를 기준으로 문자열을 나눔


