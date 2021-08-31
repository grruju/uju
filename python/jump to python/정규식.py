# 주민등록번호가 포함된 텍스트에서 뒷자리를 *로 변경해 보자.
data = """
park 8009005-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):    # <--- 공백 문자마다 나누기
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))    # <--- 나눈 단어 조립하기
print("\n".join(result))

# 정규식을 사용하면 다음처럼 훨씬 간편하고 직관적인 코드를 작성할 수 있다.
import re       # <--- 정규 표현식을 사용하기 위한 re 모듈

data = """
park 8009005-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))