import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseurl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
plusurl = input('검색어를 입력하세요 : ')
url = baseurl + urllib.parse.quote_plus(plusurl)
print(url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

print(soup)


title = soup.find_all(class_='api_txt_lines total_tit')

# for i in title:
#     print(i.text)
#     print((i.attrs['href']))
#     print()

    