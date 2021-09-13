from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.webdriver import WebDriver


baseurl = 'https://www.instagram.com/explore/tags/'
plusurl = input('검색할 태그를 입력하세요 : ')

url = baseurl + quote_plus(plusurl)

print(url)

# 크롬 드라이버
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('C:/Users/river/GrrUJU/uju/python/chromedriver.exe',options=options)
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/")

# 인스타그램 접속후, 로그인 하기

driver.find_element_by_name('username').send_keys('grruju@gmail.com') 
driver.find_element_by_name('password').send_keys('Rkdxorbsla1!') 
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()


# 아이디 / 패스워드 / 클릭 다른 소스
# driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys('grruju@gmail.com')
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys('Rkdxorbsla1!')
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()

time.sleep(2)
driver.get(url)

time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1
for i in insta:
    print('https://www.instagram.com/' + i.a['href'])
    imgurl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgurl) as f:
        with open('./python/img/' + plusurl + str(n) + '.png', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgurl)
    print(n)        
    print()

driver.close()
