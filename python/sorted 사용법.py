fruit = {'apple':5, 'grape':10, 'bnana':15, 'peeach':3, 'melon':15}

sorted1 = sorted(fruit.items(), reverse=True)

print(sorted1)

def f1(x):
    return x[0]

def f2(x):
    return x[1]

print(f2([3,5]))

sorted2 = sorted(fruit.items(), key=f1)
print(sorted2)

sorted3 = sorted(fruit.items(), key=f2, reverse=True)
print(sorted3)