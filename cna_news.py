# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:30:40 2021

@author: 100010270
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.cna.com.tw/topic/newstopic/2012.aspx'

headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

response = requests.get(url, headers=headers)
response.raise_for_status()
response.encoding = 'utf8'
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('#jsMainList')[0]

dates = [date.text for date in data.select('.date')][:5]
titles = [title.text for title in data.find_all('h2')][:5]
imgs = [img.get('data-src') for img in data.find_all('img')][:5]
links = [link.get('href') for link in data.find_all('a')][:5]



print(titles)