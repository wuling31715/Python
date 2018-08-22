from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get("http://codeta.ml/contest/10/problems")
# time.sleep(5)
# login_button = driver.find_element_by_class_name('ivu-btn-ghost').click()
username = '103306071'
password = 'pythonissoeasy'
input_list = driver.find_elements_by_class_name('ivu-input-large')
input_username = input_list[0]
input_password = input_list[1]
input_username.send_keys(username)
input_password.send_keys(password)
login_button = driver.find_element_by_class_name('ivu-btn-primary').click()
driver.get("http://codeta.ml/acm-rank")
print(driver.page_source)
driver.close()
