import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, quote_plus
import re
from requests.api import post, request
import pyautogui
import csv


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
        # print("블로그")
        return text

    elif soup.find("div", attrs={"id":"postViewArea"}):
        text = soup.find("div", attrs={"id":"postViewArea"}).get_text()
        text = text.replace("\n","") 
        return text
    else:
        return "확인불가"


query = pyautogui.prompt(title='검색어를 입력하세요.',text='검색어를 입력하세요.')

url = 'https://search.naver.com/search.naver?query='+quote_plus(query)+'&nso=&where=blog&sm=tab_opt'

# print(url)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.select("ul.lst_total > li")

bloglist = []
for post in posts:
    temp = []
    post_link = post.select_one("a.api_txt_lines.total_tit")['href']
    temp.append(post.select_one("a.api_txt_lines.total_tit").text)
    temp.append(post.select_one("a.api_txt_lines.total_tit")['href'])
    
    blog_p = re.compile("blog.naver.com")
    blog_m = blog_p.search(post_link)

    if blog_m:
        temp.append(text_scraping(delete_iframe(post_link)))
    bloglist.append(temp)
    
    with open('naverBLOG.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['제목','링크','내용'])
        writer.writerows(bloglist)

btn2 = pyautogui.alert('csv 파일 저장이 끝났습니다.','Naver Blog Save Completion')
