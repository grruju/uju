fruit = {'apple':5, 'grape':10, 'bnana':15, 'peeach':3, 'melon':12}

sorted1 = sorted(fruit.items(), key=lambda x:x[0])
sorted2 = sorted(fruit.items(), key=lambda x:x[1])

print(sorted1)
print(sorted2)