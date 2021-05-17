# -*- coding: utf-8 -*-
"""
Created on Fri May 14 09:26:19 2021

@author: 100010270
"""

import requests
from bs4 import BeautifulSoup


url = 'https://www.chcg.gov.tw/ch/news.asp?date1=2021/5/1&date2=2022/12/31&schtxt='

headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

response = requests.get(url, headers=headers)
response.raise_for_status()
response.encoding = 'utf8'
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('.list-unstyled')[19]

dates = [date.text for date in data.select('.date')][:4]
titles = [title.text.strip() for title in data.find_all('a')][:4]
links = ['https://www.chcg.gov.tw/ch/' + link.get('href').replace('./','') for link in data.find_all('a')][:4]

#https://zh.wikipedia.org/wiki/%E5%BD%B0%E5%8C%96%E7%B8%A3%E6%94%BF%E5%BA%9C#/media/File:Logo_of_Changhua_County_Government.svg



print(titles)