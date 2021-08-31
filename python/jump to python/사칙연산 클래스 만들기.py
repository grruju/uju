# 클래스 구조 만들기
class FourCal:
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


# 객체 a 만들기
a = FourCal()
print(type(a))  # 객체 a의 타입은 <class '__main__.FourCal'> 클래스이다.

# 객체에 숫자 지정할 수 있게 만들기
''' 생성된 객체 a는 아무런 기능도 하지 못한다. 우선 a객체에 사칙연산을 할 때 사용할 2개의 숫자를 먼저 지정한다. '''
a.setdata(4,2)
'''
a.setdata(4,2)로 호출하면 setdata 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달되어 다음과 같이 해석된다.
self.first = 4
self.second = 2

self는 전달된 객체 a이므로 다음과 같다.
a.first = 4
a.second = 2
'''
print(a.first)
print(a.second)

a = FourCal()
b = FourCal()

a.setdata(5,3)
print(a.first)
b.setdata(4,8)
print(b.first)

print(id(a.first))
print(id(b.first))

# add 메서드 추가

a = FourCal()
a.setdata(4,2)
print(a.add())

# mul, sub, div 메서드 추가

a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

