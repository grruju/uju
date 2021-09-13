import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import urllib.request

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
headers = {"User_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

weather = soup.select("ul.list_area._pageList > li")


for week in weather :
    now = week.select_one("span.day_info").text
    print(now)

    morning = week.select_one("span.point_time.morning").text.strip()
    print("오전 : "+morning," , ", end="")
    afternoon = week.select_one("span.point_time.afternoon").text.strip()
    print("오후 : "+afternoon," , ",end="")
    temp = week.select_one("dl").text.strip().replace(",","/")
    print(temp)