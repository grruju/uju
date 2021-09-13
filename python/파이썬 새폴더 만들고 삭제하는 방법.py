import os

try:
    os.rmtree('새폴더만들기')
    print('폴더를 삭제했습니다.')
except FileNotFoundError as c:
    print(c)

try:
    os.mkdir('새폴더만들기')
    print('폴더를 생성하였습니다.')
except FileExistsError as e:
    print(e)


print('프로그램을 종료합니다.')