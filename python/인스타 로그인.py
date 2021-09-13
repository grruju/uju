from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time

hdr = {"User-Agent": "Mozilla/5.0"}

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# # browser = webdriver.Chrome(options=options)
# driver = webdriver.Chrome('C:/Users/river/GrrUJU/uju/python/chromedriver.exe',options=options)
# driver.implicitly_wait(10)       # 드라이버 3초 대기. 중요
# driver.get('https://instagram.com/')
# time.sleep(1)


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('C:/Users/river/GrrUJU/uju/python/chromedriver.exe',options=options)
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/")
# 아이디
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys('grruju@gmail.com')
time.sleep(1)
# 비밀번호
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys('Rkdxorbsla1!')
time.sleep(1)

# 버튼 누르기
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()

time.sleep(10)

