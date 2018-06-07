# _*_ coding: utf-8 _*_
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def index1(str):
    try:
        index1 = str.index('人文通')
        return True
    except:
        return False


def index2(str):
    try:
        index2 = str.index('自然通')
        return True
    except:
        return False


def index3(str):
    try:
        index3 = str.index('社會通')
        return True
    except:
        return False


def is_general(str):
    if index1(str) or index2(str) or index3(str):
        return True

arr = range(10)
for i in range(0, len(arr)):
    print i
