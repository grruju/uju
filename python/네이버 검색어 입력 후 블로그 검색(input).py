import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, quote_plus
from requests.api import post

query = input('검색어를 입력하세요 : ')
url = 'https://search.naver.com/search.naver?query=' + quote_plus(query) + '&nso=&where=blog&sm=tab_viw.all'

print(url)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'lxml')

posts = soup.find_all("li", attrs={"class":"bx _svp_item"})


n  = 0
for post in posts:
    n += 1
    print(n)
    post_title = post.find("a", attrs={"class":"api_txt_lines total_tit _cross_trigger"}).get_text()
    print("제목 : ",post_title)
    post_link = post.find("a", attrs={"class":"api_txt_lines total_tit _cross_trigger"})['href']
    print("링크 : ",post_link)
    print("-"*100)
    print()

