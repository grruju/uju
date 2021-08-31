# sub_dir_search.py
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)
        
search("C:/")
'''
os.listdir를 사용하면 해당 디렉토리에 있는 파일들의 리스트를 구할 수 있다.(파일 이름만 포함되어 있음)
경로를 포함한 파일 이름을 구하기 위해서는 입력으로 받은 dirname을 앞에 덧붙여 주어야 한다.
디렉토리와 파일 이름을 이어 주는 os.path.join 함수를 사용하여 전체 경로를 쉽게 구할 수 있다.
'''

# 확장자가 .py인 파일만 출력하도록 변경(C:/디렉토리에 있는 모든 파이썬 파일이 출력)
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]           # 파일 이름에서 확장자만 추출하기 위해 os.path.splitext 함수 사용
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
        
search("C:/")

'''
try ... except PermissionError로 함수 전체를 감싼 이유는 os.listdir를 수행할 때 
권한이 없는 디렉토리에 접근하더라도 프로그램이 오류로 종료되지 않고 그냥 수행되도록 하기 위함이다.

full_filename이 디렉토리인지 파일인지 구별하기 위하여 os.path.isdir 함수 사용. 
디렉토리일 경우 search 함수 호출하여 하위 파일 다시 검색
'''