from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\김현지\Desktop\eclipse\python\chromedriver.exe')
driver.get('http://www.aladin.co.kr')
time.sleep(1)

# 베스트셀러 탭 클릭
driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()
time.sleep(1)

# selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기
src = driver.page_source
print(src)

# 뷰티풀수프 객체 생성
# 뷰태풀수프 객체를 생성하면서, 셀레늄이 가지고 온 html 소스코드를 제공하고,
# 해당 소스코드를 html 문법으로 변환하라는 주문
soup = BeautifulSoup(src,'html.parser')

'''
- 뷰티풀수프를 사용하여 수집하고 싶은 데이터가 들어있는 태그를 부분 추출할 수 있습니다.
- find_all() 메서드는 인수값으로 추출하고자 하는 태그의 이름을 적으면 해당 태그만 전부 추출하여 리스트에 담아 대입합니다.
'''
div_list = soup.findAll('div',class_='ss_book_box')
# print('div_list에 들어있는 데이터 수 : ', len(div_list))
# print(div_list[0]) # 1위 책만 가져와라

first_book = div_list[0].find_all('li')

# text는 태그를 제외한 사용자가 실제로 브라우저에서 확인 가능한 텍스트만을 추출하여 문자열 형태로 반환합니다.
book_title = first_book[1].text
book_author = first_book[2].text
book_price = first_book[3].text

book_info = book_author.split('|')

print('# 제목 : ',book_title)
print('# 저자 : ',book_info[0])
print('# 출판사 : ',book_info[1])
print('# 출판일 : ',book_info[2])
print('# 가격 : ', book_price.split(', ')[0])







