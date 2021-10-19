from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time
import json
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
'''
크롤링을 위해 필요한 selenium
크롤링 중간 중간 시간 지연을 두기 위한 time
크롤링한 내용 중 정규식으로 전처리 하기 위한 re
댓글, 대댓글을 저장할때 json 화 시키기 위한 json
데이터를 최종적으로 csv로 저장하기 위한 pandas 
이렇게 필요한 라이브러리를 import 해줍니다.
'''

# URL
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

'''
인스타그램 계정 로그인은 이동한 로그인 페이지에서
바로 input_form을 찾아 아이디와 비밀번호를 입력한 뒤 로그인 버튼을 찾아 클릭하면 되어 
form을 찾는 것은 find_element_by_name을 활용하여 찾았고
버튼은 find_element_by_css_selector를 활용하여 버튼의 class명으로 찾았습니다.
'''

# 아이디 / 패스워드 / 클릭 다른 소스
# driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys('grruju@gmail.com')
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys('Rkdxorbsla1!')
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()

# 로그인 과정에서 딜레이 되는 시간 벌기
time.sleep(2)
driver.get(url)     # 지연시간을 두어 검색하려는 url로 이동합니다.
time.sleep(2)

# 첫번째 게시물 
first_img_css="div.v1Nh3.kIKUG._bz0w" 
driver.find_element_by_css_selector(first_img_css).click()      # 첫번째 게시물 클릭

# data lists        변수 선언
location_infos = [] 
location_hrefs = [] 
upload_ids = [] 
date_texts = [] 
date_times = [] 
date_titles = [] 
main_texts = [] 
instagram_tags = [] 
comments = [] 
check_arrow = True 
count_extract = 0 
wish_num = 10 
instagram_tags = [] 
instagram_tag_dates = []

'''
check_arrow는 다음 게시물 버튼이 있는 지 없는 지 여부를 체크하는 bool 변수
count_extract는 현재 몇 개의 게시물을 추출했는지 체크하는 int 변수
wish_num은 최종적으로 몇 개의 게시물을 추출할 것인지에 대한 변수 입니다.
'''

location_object_css="div.o-MQd.z8cbW > div.M30cS > div.JF9hh > a.O4GlU" 
upload_id_object_css="div.e1e1d > span.Jv7Aj.MqpiF > a.sqdOP.yWX7d._8A5w5.ZIAjV " 
date_object_css="div.k_Q0X.NnvRN > a.c-Yi7 > time._1o9PC.Nzb55" 
main_text_object_css="div.C7I1f.X7jCj > div.C4VMK > span" 
tag_css=".C7I1f.X7jCj" 
comment_more_btn="button.dCJp8.afkep" 
comment_ids_objects_css="ul.Mr508 > div.ZyFrc > li.gElp9.rUo9f > div.P9YgZ > div.C7I1f > div.C4VMK > h3" 
comment_texts_objects_css="ul.Mr508 > div.ZyFrc > li.gElp9.rUo9f > div.P9YgZ > div.C7I1f > div.C4VMK > span" 
print_flag=False 
next_arrow_btn_css1="._65Bje.coreSpriteRightPaginationArrow" 
next_arrow_btn_css2="._65Bje.coreSpriteRightPaginationArrow" 
while True:
    if count_extract > wish_num:
        break 
    time.sleep(5.0) 

    # 위치정보 
    if check_arrow == False:        # check_arrow는 다음 게시물 버튼이 있는 지 없는 지 여부를 체크하는 bool 변수
        break 
    try: 
        location_object = driver.find_element_by_css_selector(location_object_css) 
        location_info = location_object.text 
        location_href = location_object.get_attribute("href") 
    except: 
        location_info = None 
        location_href = None 

    # 올린사람 ID 
    try: 
        upload_id_object = driver.find_element_by_css_selector(upload_id_object_css) 
        upload_id = upload_id_object.text 
    except: 
        upload_id = None 

    # 날짜 
    try: 
        date_object = driver.find_element_by_css_selector(date_object_css) 
        date_text = date_object.text 
        date_time = date_object.get_attribute("datetime") 
        date_title = date_object.get_attribute("title") 
    except: 
        date_text = None 
        date_time = None 
        date_title = None 
        
    # 본문 
    try: 
        main_text_object = driver.find_element_by_css_selector(main_text_object_css) 
        main_text = main_text_object.text 
    except: 
        main_text = None 
    
    ## 본문 속 태그 
    try: 
        data = driver.find_element_by_css_selector(tag_css) # C7I1f X7jCj 
        tag_raw = data.text 
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw) 
        tag = ''.join(tags).replace("#"," ") # "#" 제거 
        
        tag_data = tag.split() 
        
        for tag_one in tag_data: 
            instagram_tags.append(tag_one) 
    except: 
        continue 
    
    # 댓글 
    # ## 더보기 버튼 클릭 
    try: 
        while True: 
            try: 
                more_btn = driver.find_element_by_css_selector(comment_more_btn) 
                more_btn.click() 
            except: 
                break 
    except: 
        print("----------------------fail to click more btn----------------------------------") 
        continue 
    
    ## 댓글 데이터 
    try: 
        comment_data = {} 
        comment_ids_objects = driver.find_elements_by_css_selector(comment_ids_objects_css) 
        comment_texts_objects = driver.find_elements_by_css_selector(comment_texts_objects_css) 
        try: 
            for i in range(len(comment_ids_objects)): 
                comment_data[str((i+1))] = {"comment_id":comment_ids_objects[i].text, "comment_text":comment_texts_objects[i].text} 
        except: 
            print("fail") 
            
    except: 
        comment_id = None 
        comment_text = None 
        comment_data = {} 
    try: 
        if comment_data != {}: 
            keys = list(comment_data.keys()) 
            
            for key in keys: 
                if comment_data[key]['comment_id'] == upload_id: 
                    tags = re.findall('#[A-Za-z0-9가-힣]+', comment_data[key]['comment_text']) 
                    tag = ''.join(tags).replace("#"," ") # "#" 제거 
                    
                    tag_data = tag.split() 
                    
                    for tag_one in tag_data:
                        instagram_tags.append(tag_one) 
    except: 
        continue 
    
    location_infos.append(location_info) 
    location_hrefs.append(location_href) 
    upload_ids.append(upload_id) 
    date_texts.append(date_text) 
    date_times.append(date_time) 
    date_titles.append(date_title) 
    main_texts.append(main_text) 
    comment_json = json.dumps(comment_data) 
    comments.append(comment_json) 
    
    if print_flag: 
        print("location_info : ", location_info) 
        print("location_href : ", location_href) 
        print("upload id : ", upload_id) 
        print("date : {} {} {}".format(date_text, date_time, date_title)) 
        print("main : ", main_text) 
        print("comment : ", comment_data) 
        print("insta tags : ", instagram_tags) 
        
    try: 
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_arrow_btn_css1))) 
        driver.find_element_by_css_selector(next_arrow_btn_css2).click() 
    except: 
        check_arrow = False 
    count_extract += 1

'''
위치정보, 게시한 사람 ID, 날짜, 본문, 본문 속 태그, 댓글 정보를 추출합니다.
print_flag를 True로 주면 추출하는 정보를 실시간으로 출력합니다.
게시물 하나 추출할 때마다 count_extract를 1씩 증가시키고
wish_num 보다 커질 경우 추출을 멈춥니다.
'''

# 추출한 정보 저장
save_file_name="instagram_extract" 
save_file_name_tag="instagram_tag" 

try: 
    insta_info_df = pd.DataFrame({"location_info":location_infos, "location_href":location_hrefs, "upload_id":upload_ids, "date_text":date_texts, "date_time":date_times, "date_title":date_titles, "main_text":main_texts, "comment":comments}) 
    insta_info_df.to_csv("{}.csv".format(save_file_name), index=False) 
except: 
    print("fail to save data") 


try: 
    insta_tag_df = pd.DataFrame({"tag":instagram_tags}) 
    insta_tag_df.to_csv("{}.csv".format(save_file_name_tag), index=False) 
except: 
    print("fail to save tag data") 

time.sleep(5)

driver.close() 
driver.quit()


# html = driver.page_source
# soup = BeautifulSoup(html)

# insta = soup.select('.v1Nh3.kIKUG._bz0w')

# n = 1
# for i in insta:
#     print('https://www.instagram.com/' + i.a['href'])
#     imgurl = i.select_one('.KL4Bh').img['src']
#     with urlopen(imgurl) as f:
#         with open('./python/img/' + plusurl + str(n) + '.png', 'wb') as h:
#             img = f.read()
#             h.write(img)
#     n += 1
#     print(imgurl)
#     print(n)        
#     print()

'''
함수명 설명 
find_element_by_id                  요소의 속성 id로 찾는 오브젝트를 찾습니다. 
find_element_by_class_name          요소의 속성 class가 포함된 오브젝트를 찾습니다. 
find_element_by_name                요소의 속성 name로 찾는 오브젝트를 찾습니다. 
find_element_by_xpath               xpath를 이용해서 오브젝트를 찾습니다. 
find_element_by_link_text           하이퍼 링크의 텍스트로 오브젝트를 찾습니다.(완전 일치) - 탐색이 잘 안됩니다. 
find_element_by_partial_link_text   하이퍼 링크의 텍스트로 오브젝트를 찾습니다.(포함) - 탐색이 잘 안됩니다. 
find_element_by_tag_name            요소의 태그 이름으로 찾습니다. 
find_element_by_css_selector        css selector(sizzle)로 오브젝트를 찾습니다.
'''