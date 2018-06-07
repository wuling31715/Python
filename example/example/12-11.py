
# _*_ coding: utf-8 _*_
# 程式 12-11 (Python 3 Version)

import requests, jieba, operator
from bs4 import BeautifulSoup

url = 'https://www.inside.com.tw/2017/02/19/bill-gates-job-stealing-robots-should-pay-income-taxes'

news_page = requests.get(url)
news = BeautifulSoup(news_page.text, 'html.parser')

news_title = news.find_all('div', {'class': 'container'})

headlines = ''
for t in news_title:
    title = t.find_all('a')[0]
    headlines += title.text

words = jieba.cut(headlines)

word_count = dict()

for word in words:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

    sorted_wc = sorted(
        word_count.items(), key=operator.itemgetter(1), reverse=True)

for item in sorted_wc:
    if item[1] > 1:
        print item[0], item[1]
    else:
        break
