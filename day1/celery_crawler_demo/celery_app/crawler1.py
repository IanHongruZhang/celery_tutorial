# -*- coding:utf-8 -*-

import time
import requests
import logging
from celery_app import app
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#url = "https://www.thepaper.cn/"

def requests_page(url):
    ua = UserAgent()
    headers = {"User-Agent":ua.random} #设置一个伪造请求头
    response_text = requests.get(url,headers = headers).text
    response_soup = BeautifulSoup(response_text,'lxml')
    return response_soup

@app.task
def crawl_thepaper(url):
    response_soup = requests_page(url)
    all_news = response_soup.find('div',class_ = "newsbox").find_all("h2")
    all_news_title = list(map(lambda x:x.find("a").get_text(),all_news))
    for title in all_news_title:
    	logging.error(title) #暂时使用logging.error()代替print()
    	time.sleep(1) #使得所有结果不要一下子全部在terminal上显示
