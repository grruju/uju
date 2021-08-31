f = open("c:/Users/river/Python/새파일2.txt",'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)       # <--- f의 write 함수를 사용하여 파일에 결과값을 저장
f.close()