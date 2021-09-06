fruit = ['apple', 'banana', 'melon', 'kiwi', 'grape', 'strawberry', 'orange']

print(list(enumerate(fruit)))

# 1번. enumerate 사용
for e, i in enumerate(fruit):
    print(e,i)
    if e == 3:
        break

# 2번. enumerate 사용 안했을때
e = 0
for i in fruit:
    print(e, i)
    if e == 3:
        break
    e = e + 1