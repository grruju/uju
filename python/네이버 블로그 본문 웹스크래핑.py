import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, quote_plus
import re
from requests.api import post, request


def delete_iframe(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    src_url = "http://blog.naver.com/" + soup.iframe["src"]

    return src_url

# 본문 스크래핑
def text_scraping(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")

    if soup.find("div",attrs={"class":"se-main-container"}):
        text = soup.find("div", attrs={"class":"se-main-container"}).get_text()
        text = text.replace("\n","")    # 공백 제거
        print("블로그")
        return text

    elif soup.find("div", attrs={"id":"postViewArea"}):
        text = soup.find("div", attrs={"id":"postViewArea"}).get_text()
        text = text.replace("\n","") 
        return text
    else:
        return "확인불가"


query = input('검색어를 입력하세요 : ')
# url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=' + quote(query)

url = 'https://search.naver.com/search.naver?query='+quote_plus(query)+'&nso=&where=blog&sm=tab_opt'

print(url)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.select("ul.lst_total > li")

print(posts)
n  = 0
for post in posts:
    n += 1
    print(n)
    post_title = post.select_one("a.api_txt_lines.total_tit").get_text()
    print("제목 : ",post_title)
    post_link = post.select_one("a.api_txt_lines.total_tit")['href']
    print("링크 : ",post_link)

    blog_p = re.compile("blog.naver.com")
    blog_m = blog_p.search(post_link)

    if blog_m:
        blog_text = text_scraping(delete_iframe(post_link))
        print(blog_text)
    print("-"*100)
    print()


