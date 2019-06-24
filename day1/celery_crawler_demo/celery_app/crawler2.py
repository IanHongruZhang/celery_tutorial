# -*- coding:utf-8 -*-

import time
import requests
import logging
from celery_app import app
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def requests_page(url):
    ua = UserAgent()
    headers = {"User-Agent":ua.random} #设置一个伪造请求头
    response_text = requests.get(url,headers = headers).text
    response_soup = BeautifulSoup(response_text,'lxml')
    return response_soup

@app.task
def crawl_jiemian(url):
    response_soup = requests_page(url)
    all_tops = response_soup.find("div", class_="news-list")
    for item in all_tops:
    	for text in item:
    		logging.error(text.get_text()) #暂时使用logging.error()代替print()
    		logging.error("\n")
    		time.sleep(1) #使得所有结果不要一下子全部在terminal上显示