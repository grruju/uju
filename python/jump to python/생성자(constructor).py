# 클래스 구조 만들기
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):       # 클래스 안에 구현된 함수는 매서드(Method) 라고 한다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        resutl = self.first / self.second
        return resutl
        
# 생성자(Constructor)
'''
__init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 단 메서드 이름을 __ini__ 으로 했기 떄문에 
생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.
'''
a = FourCal(4,2)

print(a.first)
print(a.second)

print(a.add())
print(a.div())


# 클래스의 상속
''' 
클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어 주면 된다.
class 클래스 이름(상속할 클래스 이름)
'''

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(a.pow())

# 매서드 오버라이딩
''' 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것. '''
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:    # <--- 나누는 값이 0인 경우 숫자 0을 돌려주도록 수정
            return 0
        else:
            return self.first / self.second

''' 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 출력된다. '''

a = SafeFourCal(4,0)
print(SafeFourCal.div(a))
print(a.div())

