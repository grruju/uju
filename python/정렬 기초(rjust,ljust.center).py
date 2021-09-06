fruit = {'apple':5, 'banana':8, 'grape':7, 'orage':3, 'peach':10}

for k, v in fruit.items():
    print(k.ljust(10, '-') + str(v).rjust(5))   # v는 int이기 떄문에 오류나서 str로 변환

    