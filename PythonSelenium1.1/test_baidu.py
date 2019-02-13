# -*- coding: utf8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/Users/miaog001/Documents/AutoProjects/chromedriver')
driver.get("http://www.baidu.com")
searchField = driver.find_element_by_id("kw")
searchField.clear()
searchField.send_keys(u"Automation")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.close()