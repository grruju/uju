a = "20210728Rainy"
year = a[0:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]

print(year)
print(month)
print(day)
print(weather)

print(year + '년 ' + month + '월 ' + day + '일 ' + '날씨 ' + weather)