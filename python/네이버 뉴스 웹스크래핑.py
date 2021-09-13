import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
search = quote_plus(input('검색어를 입력하세요 : '))    

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=" + search + 'start=' + str(n),  headers=headers)
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.list_news > li")

    # title = articles[0].select_one("a.news_tit").text
    # print(title)
    # body = articles[0].select_one("a.api_txt_lines.dsc_txt_wrap").text
    # print(body)
    # link = articles[0].select_one("a.news_tit")['href']
    # print(link)

    for news in articles :
        n += 1
        n2 = n-1
        link = news.select_one("a.news_tit")['href']
        title = news.select_one("a.news_tit").text
        body = news.select_one("a.api_txt_lines.dsc_txt_wrap").text
        print(n2)
        print('-'*100)
        print(link)
        print(title)
        print(body)
        print('-'*100)
        print()
