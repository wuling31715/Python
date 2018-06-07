# _*_ coding: utf-8 _*_

import requests, uniout, sys

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = raw_input("請輸入要查詢的姓名:")
html = requests.get(url).text
if name in html:
    print("恭喜名列金榜")
else:
    print("不好意思，榜單中找不到{}".format(name))
