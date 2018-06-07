# _*_ coding: utf-8 _*_
from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib.pyplot as pt
import time


def score_to_gpa(score):
    if score >= 0 and score < 50:
        gpa = 0.0
    elif score >= 50 and score < 53:
        gpa = 0.7
    elif score >= 53 and score < 57:
        gpa = 1.0
    elif score >= 57 and score < 60:
        gpa = 1.3
    elif score >= 60 and score < 63:
        gpa = 1.7
    elif score >= 63 and score < 66:
        gpa = 2.0
    elif score >= 66 and score < 70:
        gpa = 2.3
    elif score >= 70 and score < 73:
        gpa = 2.7
    elif score >= 73 and score < 77:
        gpa = 3.0
    elif score >= 77 and score < 80:
        gpa = 3.3
    elif score >= 80 and score < 85:
        gpa = 3.7
    elif score >= 85 and score < 90:
        gpa = 4.0
    elif score >= 90 and score <= 100:
        gpa = 4.3
    else:
        gpa = 0.0
    return gpa


def str_to_float(str):
    try:
        return float(str)
    except:
        return 0.0


def average_count(credit_arr, score_arr):
    score_sum = 0.0
    credit_sum = 0.0
    for i in range(0, len(credit_arr)):
        score_sum = score_sum + (credit_arr[i] * score_arr[i])
        credit_sum = credit_sum + credit_arr[i]
    score_average = score_sum / credit_sum
    return score_average, credit_sum


def gpa_count(credit_arr, credit_sum, gpa_arr):
    gpa_sum = 0.0
    for i in range(0, len(credit_arr)):
        gpa_sum = gpa_sum + (credit_arr[i] * gpa_arr[i])
    gpa_average = gpa_sum / credit_sum
    return gpa_average


def index1(str):
    try:
        index1 = str.index('人文通')
        return True
    except:
        pass


def index2(str):
    try:
        index2 = str.index('自然通')
        return True
    except:
        pass


def index3(str):
    try:
        index3 = str.index('社會通')
        return True
    except:
        pass


def is_general(str):
    if index1(str) or index2(str) or index3(str):
        return True


def get_data(account, password):
    account = account
    password = password

    browser.get('https://i.nccu.edu.tw/Login.aspx?ReturnUrl=%2fdefault.aspx')
    browser.maximize_window()
    time.sleep(1)
    input_account = browser.find_element_by_id('captcha_Login1_UserName')
    input_account.clear()
    input_account.send_keys(account)

    browser.find_element_by_id('captcha_Login1_Password').clear()
    browser.find_element_by_id('captcha_Login1_Password').send_keys(password)
    browser.find_element_by_id('captcha_Login1_LoginButton').click()
    time.sleep(1)
    browser.get(
        'http://i.nccu.edu.tw/sso_app/PersonalInfoSSO.aspx?p=2&sid=%s' % (account))
    time.sleep(3)
    bs = BeautifulSoup(browser.page_source, "lxml")
    div = bs.find_all('div', attrs={"align": "left"})
    arr_all = []
    arr_credit = []
    arr_score = []
    arr_grade = []

    for row in div:
        if is_general(row.text):
            pass
        else:
            arr_all.append(row.text)

    for row in arr_all:
        if arr_all.index(row) % 7 == 5:
            arr_credit.append(row)
        elif arr_all.index(row) % 7 == 6:
            arr_score.append(row)

    return arr_all, arr_credit, arr_score


def data_print():
    for i in range(0, len(credit_all)):
        print(credit_all[i], score_all[i], gpa_all[i])


def diagram_print(x, y, gpa):
    pt.bar(x, y, label=gpa, color='red')
    pt.xlabel('Grade')
    pt.ylabel('Score')
    pt.legend()
    pt.title('GPA')
    pt.show()


account = str(input())
password = str(input())

browser = webdriver.Firefox(
    executable_path='/Users/dannyshau/code/python/driver/geckodriver')

browser.maximize_window()
data_all_str = get_data(account, password)
credit_all_str = data_all_str[1]
credit_all_str.reverse()
score_all_str = data_all_str[2]
score_all_str.reverse()

credit_all = []
score_all = []
gpa_all = []
grade_all = []
for i in range(0, len(credit_all_str)):
    if str_to_float(credit_all_str[i]) > 0.0 and str_to_float(
            score_all_str[i]) > 0.0:
        credit_all.append(str_to_float(credit_all_str[i]))
        score_all.append(str_to_float(score_all_str[i]))

for i in range(0, len(score_all)):
    gpa_all.append(score_to_gpa(score_all[i]))

score_average = average_count(credit_all, score_all)[0]
credit_sum = average_count(credit_all, score_all)[1]
gpa_average = gpa_count(credit_all, credit_sum, gpa_all)
grade_all = range(len(gpa_all))

print('總平均 = %s' % score_average)
print('總學分 = %s' % credit_sum)
print('總科目 = %s' % len(grade_all))
print('GPA = %s' % gpa_average)

browser.quit()
diagram_print(grade_all, gpa_all, gpa_average)
