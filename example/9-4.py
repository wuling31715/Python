# _*_ coding: utf-8 *_*
# 程式 9-4 (Python 3 version)

import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

url = 'http://exp.management.ntu.edu.tw/zh-TW/IM/teachers/16'

html = requests.get(url).text

emails = re.findall(regex, html)
for email in emails:
    print(email)

print html
