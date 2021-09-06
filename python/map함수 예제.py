# map은 리스트 등 반복 할 수 있는 항목을 함수에 적용해서 그 결과를 돌려줍니다.
def f(x):
    return x + 5

numList = [1, 2, 3, 4, 5]

print(numList)
print(map(f, numList))

print(list(map(f, numList)))

