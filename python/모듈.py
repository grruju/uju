# 모듈 불러오기
''' 콘솔에서 
1. import 모듈이름 
2. form 모듈이름 import 모듈함수
ex) from mod1 import * (모든 모듈함수 임포트)
'''

#  if __name_ == "__main__" :  의 의미
'''
if __name__ == "__main__" 을 사용하면 c:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는
__name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다. 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서
사용할 때는 __name__ == "__min__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.
'''

# 다른 파일에서 모듈 불러오기
# modtest.py
import mod2                 # 동일 디렉토리에 있어야 한다.
result = mod2.add(3,4)
print(result)

