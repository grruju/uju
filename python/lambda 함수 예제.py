add = lambda x,y : x+y
print(add(3,4))
print(add(5,7))

# 람다 함수의 특징. 리스트를 사용할 수 있다.

lambdas = [lambda x:x+10, lambda x:x+100]

print(lambdas[0](5))    # lambda x:x+10
print(lambdas[1](5))    # lambda x:x+100
