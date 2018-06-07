from bs4 import BeautifulSoup
import requests, sys

reload(sys)
sys.setdefaultencoding('utf-8')

def web_parser(url):
    links = []
    html = requests.get(url).text
    sp = BeautifulSoup(html, 'html.parser')
    a = sp.find_all('a')
    for row in a:
        href = row.get('href')
        if href != None and href.startswith('http://'):
            links.append(href)
    return links

print web_parser('http://moltke.cc.nccu.edu.tw/selfDevelop_SSO/lessionStudyDataList.selfDevelop')
