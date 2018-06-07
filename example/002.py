# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver(executable_path='/Users/dannyshau/code/python/driver/geckodriver')
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://i.nccu.edu.tw/Login.aspx?ReturnUrl=/Home.aspx")
    wd.find_element_by_id("captcha_Login1_Password").click()
    wd.find_element_by_id("captcha_Login1_Password").send_keys("\\undefined")
    wd.find_element_by_id("captcha_Login1_LoginButton").click()
    wd.find_element_by_id("WidgetContainer554210_Widget554210_HyperLink2").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
