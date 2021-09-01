# from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import requests

# html = urlopen("https://news.naver.com/")
html = "https://news.naver.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

r = requests.get(html, headers=headers)

bsObject = BeautifulSoup(r.text, 'html.parser')

for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))

for link in bsObject.find_all('img'):
    print(link.text.strip(), link.get('src'))