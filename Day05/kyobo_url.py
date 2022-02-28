import codecs
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime

# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
from fake_useragent import UserAgent

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req

d = datetime.today()
file_path = f'C:/test/crawling/교보문구_{d.year}_{d.month}_{d.day}.html'
with codecs.open(file_path , mode='w' ,encoding='utf-8') as f:
  browser = webdriver.Chrome('C:/test/crawling/chromedriver.exe')
  browser.get('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79')

  time.sleep(1.5)

  src =  browser.page_source
  soup = BeautifulSoup(src, 'html.parser')
  title_list = soup.find_all('div', class_='title')
  print(title_list)

  rank = 1

  f.write('<!DOCTYPE HTML> \r\n')
  f.write('<html> \r\n')
  f.write('<head> \r\n')
  f.write('<meta charset="UTF-8"> \r\n')
  f.write('<title> 교보문고 베스트 셀러 1~20위</title> \r\n')
  f.write('<body> \r\n')

  for idx in range(len(title_list)):
    if idx > 31:
      f.write('<p style="font-size : 20px"> \r\n')
      f.write(f'<b>순위 : {rank}위</b> <br> \r\n')
      a_url = str(title_list[idx].find('a')) 
      f.write(a_url + '\n <hr> \n')
      rank += 1
      f.write('</p>')

  f.write('</body> \r\n')
  f.write('</html>')









