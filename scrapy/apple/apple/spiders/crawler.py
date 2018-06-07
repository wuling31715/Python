import scrapy
import requests
import csv

from bs4 import BeautifulSoup
from scrapy.http import Request, FormRequest
'''
class AppleCrawler(scrapy.Spider):
    name = 'apple'
    start_urls = ['http://www.appledaily.com.tw/realtimenews/section/new/']
    def parse(self, response):
        with open('apple/data/test.csv', 'a') as csvfile:
            fieldnames = ['title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            res = BeautifulSoup(response.body)
            for row in res.select('.rtddt'):
                print(row.select('h1')[0].text)
                title = row.select('h1')[0].text
                writer.writerow({fieldnames[0]: title})
'''

#https://m.facebook.com/profile.php?v=info&id=100002379548465
#https://m.facebook.com/profile.php?v=info&id=1008401422
#https://m.facebook.com/dannyhsiao.tw?v=info
#1287160323


class FacebookSpider(scrapy.Spider):
    name = 'apple'
    email = 'wuling31715@gmai.com'
    password = 'facebook10152017'
    csv_personal_information = 'data/personal_information.csv'
    urls = [
        'https://m.facebook.com/profile.php?v=info&id=100002379548465',
        'https://m.facebook.com/profile.php?v=info&id=1008401422',
        'https://m.facebook.com/profile.php?v=info&id=1287160323',
        'https://m.facebook.com/dannyhsiao.tw?v=info',
    ]

    def start_requests(self):
        with open(self.csv_personal_information, 'a') as csvfile:
            fieldnames = [
                'name', 'work', 'education', 'gender', 'gender_like', 'blood',
                'birthday', 'website', 'email', 'url'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        return [
            Request(
                "https://m.facebook.com/login.php",
                meta={'cookiejar': 1},
                callback=self.post_login)
        ]

    def post_login(self, response):
        return [
            FormRequest.from_response(
                response,  #"https://m.facebook.com/login.php",
                meta={'cookiejar': response.meta['cookiejar']},
                formdata={'email': self.email,
                          'pass': self.password},
                callback=self.after_login, )
        ]

    def after_login(self, response):
        for row in self.urls:
            yield scrapy.Request(
                row,
                meta={'cookiejar': response.meta['cookiejar']},
                callback=self.parse_personal_information)

    def parse_personal_information(self, response):
        body = BeautifulSoup(response.body.decode())
        about = {}

        name = body.find_all("strong")
        for row in name:
            about['name'] = row.text
            print(row.text)

        work = body.find_all("div", {"id": 'work'})
        for row in work:
            about['work'] = row.text[4:]
            print(row.text[4:])

        education = body.find_all("div", {"id": 'education'})
        for row in education:
            about['education'] = row.text[2:]
            print(row.text[2:])

        gender = body.find_all("div", {"title": '性別'})
        for row in gender:
            about['gender'] = row.text[2:]
            print(row.text[2:])

        gender_like = body.find_all("div", {"title": '戀愛性向'})
        for row in gender_like:
            about['gender_like'] = row.text[4:]
            print(row.text[4:])

        blood = body.find_all("div", {"title": '血型'})
        for row in blood:
            about['blood'] = row.text[2:-1]
            print(row.text[2:-1])

        birthday = body.find_all("div", {"title": '生日'})
        for row in birthday:
            about['birthday'] = row.text[2:]
            print(row.text[2:])

        website = body.find_all("div", {"title": '網站'})
        for row in website:
            about['website'] = row.text[2:]
            print(row.text[2:])

        email = body.find_all("div", {"title": '電子郵件'})
        for row in email:
            about['email'] = row.text[4:]
            print(row.text[4:])

        about['url'] = response.url
        print(response.url)

        try:
            about['work']
        except:
            about['work'] = None
        try:
            about['education']
        except:
            about['education'] = None
        try:
            about['gender']
        except:
            about['gender'] = None
        try:
            about['gender_like']
        except:
            about['gender_like'] = None
        try:
            about['blood']
        except:
            about['blood'] = None
        try:
            about['birthday']
        except:
            about['birthday'] = None
        try:
            about['website']
        except:
            about['website'] = None
        try:
            about['email']
        except:
            about['email'] = None
        try:
            about['url']
        except:
            about['url'] = None


        with open(self.csv_personal_information, 'a') as csvfile:
            fieldnames = [
                'name', 'work', 'education', 'gender', 'gender_like', 'blood',
                'birthday', 'website', 'email', 'url'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #writer.writeheader()
            writer.writerow({
                fieldnames[0]: about['name'],
                fieldnames[1]: about['work'],
                fieldnames[2]: about['education'],
                fieldnames[3]: about['gender'],
                fieldnames[4]: about['gender_like'],
                fieldnames[5]: about['blood'],
                fieldnames[6]: about['birthday'],
                fieldnames[7]: about['website'],
                fieldnames[8]: about['email'],
                fieldnames[9]: about['url'],
            })
