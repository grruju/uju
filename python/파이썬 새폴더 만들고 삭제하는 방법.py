import os       
import shutil   


try:
    # os.rmdir('새폴더만들기')        # os모듈에선 하위디렉토리 삭제가 불가능
    shutil.rmtree('새폴더만들기')   # shutil에서는 rmtree로 가능
    print('폴더를 삭제했습니다.')
except FileNotFoundError as c:
    print(c)

try:
    os.mkdir('새폴더만들기')
    print('폴더를 생성하였습니다.')
except FileExistsError as e:
    print(e)


print('프로그램을 종료합니다.')



# Traceback (most recent call last):
#   File "c:\Users\river\GrrUJU\uju\python\파이썬 새폴더 만들고 삭제하는 방법.py", line 4, in <module>
#     os.rmdir('새폴더만들기')
# OSError: [WinError 145] 디렉터리가 비어 있지 않습니다: '새폴더만들기'

# os 모듈에서는 폴더안에 파일이 존재할시 rmdir 로 폴더 삭제가 불가능하다.
# 따라서. 폴더안에 파일 삭제 후 다시 폴더 삭제를 진행해야 한다.

