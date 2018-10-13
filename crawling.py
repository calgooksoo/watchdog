# -*- encoding: utf-8 -*-

from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# 명시적 대기를 위해 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from DbMgr import DBHelper as Db
import time

import urllib.request
import urllib.parse
import requests
from datetime import datetime


print(datetime.now())

#from Tour import TourInfo

# 사전에 필요한 정보를 로드 => 디비혹스 쉘, 베치 파일에서 인자로 받아서 세팅
#db       = Db()
shanghai_url = 'https://quotes.sina.cn/hs/company/quotes/view/sh000001' 
snpFuture_url = 'https://www.investing.com/indices/us-spx-500'
nasdaqFuture_url = 'https://www.investing.com/indices/nq-100'
dowFuture_url = 'https://www.investing.com/indices/us-30'
eustockFuture_url = 'https://www.investing.com/indices/eu-stoxx50'
major_indice = 'https://www.investing.com/indices/major-indices'


'''
driver = wd.Chrome(executable_path='chromedriver.exe')
#driver = wd.PhantomJS(executable_path='phantomjs.exe')

driver.get(shanghai_url)
html = driver.page_source.encode('cp949', errors='replace')

soup = bs(html, 'html.parser')
a = soup.find(id="HQBox_Point_price") 
b = soup.find(id="HQBox_Point_change") 
c = soup.find(id="HQBox_Point_percent") 

shanghai_value = [] 

for title in a:
    shanghai_value.append(title)
for title in b:
    shanghai_value.append(title)
for title in c:
    shanghai_value.append(title)

print(shanghai_value)
'''


driver = wd.Chrome(executable_path='chromedriver.exe')
#driver = wd.PhantomJS(executable_path='phantomjs.exe')

driver.get(major_indice)
#dow
b = driver.find_element_by_css_selector('.pid-169-last')
print(b.text)

b = driver.find_element_by_css_selector('.bold.greenFont.pid-169-pc')
print(b.text)

b = driver.find_element_by_css_selector('.bold.greenFont.pid-169-pcp')
print(b.text)
