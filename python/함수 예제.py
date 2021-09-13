def add_num(a,b):
    return a + b


i = add_num(3,4)

print(i)

print(i+5)

def add_num2(*args) :
    return args #   아규먼트 약자?

print(add_num2(1,2,3,4,5,6,7))

def input_me(name='choi', age=20):
    return name, age

print(input_me('kim', 20))
print(input_me('lee'))
print(input_me(age=10))

def input_me2(**kwargs):
    return kwargs

print(input_me2(name='kim', age='20'))
print(type(input_me2(name='kim', age='20')))
print(input_me2(name='kim', age='20', food='pizza'))
