import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

r = requests.get(url, headers=headers)

# print(r.text)
# print(r.request.headers)

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup)

# article = soup.select('#today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a')
# article = soup.select_one('#today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a')
# select_one은 주어진 selector로 추출되는 가장 첫번째 값만 돌려준다.
article = soup.select('a.lnk_hdline_article')
# art = article[0]

# print(art)
print(article)

# title = article.text

# print(title)

# link = article.get('href')

# print(link)

# print(url+link)


for item in article:
    link = url + item.get('href')
    # print(title, link)
    title = item.text.replace("\n","").strip()
    print(title, link)


