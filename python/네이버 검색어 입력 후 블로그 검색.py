import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, quote_plus

from requests.api import post

query = input("검색어를 입력하세요 : ")
url = 'https://search.naver.com/search.naver?where=blog&sm=tab_jum&query=' + quote_plus(query)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

blog = soup.select("ul.lst_total > li")

# body = blog[0].select_one("div.api_txt_lines.dsc_txt").text

# print(body)

n  = 0
for post in blog:
    n += 1
    print(n)
    post_title = post.find("a", attrs={"class":"api_txt_lines total_tit"}).get_text()
    print("제목 : ",post_title)
    body = post.select_one("div.api_txt_lines.dsc_txt").text
    print("내용 : ",body)
    link = post.select_one("a.api_txt_lines.total_tit")["href"]
    print("링크 : ",link)
    print("-"*100)
    print()
