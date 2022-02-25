'''
네이버로 접속하셔서 뉴스스탠드 위쪽에 있는 파란색 '뉴스홈' 링크를
클릭하세요.

상단에 있는 메뉴 중 정치, 경제, 사회, 생활/문화, 세계, IT/과학
탭을 돌아다니면서 헤드라인 뉴스 4개씩 클릭해 주시면 됩니다.
뒤로가기는 driver.back() 메서드로 뒤로가기 가능합니다.

XPATH를 따다 보면 규칙을 발견하실 수 있을 겁니다.
반복문 이용해서 클릭 명령을 내려 주시면 됩니다.
24개의 명령을 일일히 쓰라는 게 아니에요. 규칙을 꼭 발견 하세요.
'''
from selenium import webdriver 
import time

driver = webdriver.Chrome(r'C:\Users\김현지\Desktop\eclipse\python\chromedriver.exe')

driver.get('http://www.naver.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[2]/a/span').click() #정치

for x in range(3,8):

  for n in range(1,5):
    if x > 5:
      i =2
    else:
      i =1

    try:
      news_head = f'//*[@id="main_content"]/div/div[2]/div[1]/div[{n}]/div[{i}]/ul/li[1]/div[2]/a'
      driver.find_element_by_xpath(news_head).click()
      time.sleep(0.7)
      driver.back()
    except:
      news_head = f'//*[@id="main_content"]/div/div[2]/div[1]/div[{n}]/div[{i}]/ul/li[1]/div/a'
      driver.find_element_by_xpath(news_head).click()
      time.sleep(0.7)
      driver.back()

  # 타분야 탭 누르는 동작
  data = f'//*[@id="lnb"]/ul/li[{x}]/a/span'
  driver.find_element_by_xpath(data).click()
  time.sleep(0.5) 
 
