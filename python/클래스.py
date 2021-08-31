result = 0

def add(num):
    global result
    result += num   # <--- result = result + num
    return result

print(add(3))
print(add(4))

# 만약 한 프로그램에서 2대의 계산기가 필요한 상황이라면?

result1 = 0
result2 = 0

def add1(num):          # 계산기1
    global result1
    result1 += num
    return result1

def add2(num):          # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

''' 계산기가 추가 필요할때마다 전역변수와 함수를 추가할 수 없으니... 클래스로 만들어서 사용. '''

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self,num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal1.sub(3))
print(cal1.sub(1))
