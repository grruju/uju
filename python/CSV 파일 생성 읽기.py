import csv

# a = 추가
# w = 새로 생성
# r = 읽기

f = open('sample.csv','w',encoding='ansi', newline='')    
# newline='' 윈도우에서 csv 파일 생성시 줄바꿈 문제가 발생하며 빈 줄이 생김. 그걸 없애주는 옵션
wr = csv.writer(f)
# wr.writerow(['r','ㅠ','ㅊ'])
wr.writerows([[1,2,3],[4,5,6],[7,8,9]]) #여러줄 입력
f.close()


f = open('sample.csv','r',encoding='ansi')
rd = csv.reader(f)
# print(rd)   # csv 리더로 읽어드린 객체 <_csv.reader object at 0x00000257DD4F4A60>. 원하는 결과값이 아니기에 의미가 없다.
for i in rd:
    print(i)
    print(type(i)) # list를 출력하기 위해 반복문으로 작성.
f.close()
