from behave import Given, When, Then, Step, use_step_matcher
from selenium import webdriver
import time
use_step_matcher("re")

@Step("I want to login baidu website")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='/Users/miaog001/Documents/AutoProjects/chromedriver')
    context.driver.get("http://www.baidu.com")


@Step("I want to enter automation in search field")
def step_impl(context):
    searchField = context.driver.find_element_by_id("kw")
    searchField.clear()
    searchField.send_keys(u"Automation")


@Step("I want to click search button")
def step_impl(context):
    context.driver.find_element_by_id("su").click()
    time.sleep(3)


@Step("I want to stop test and close browser")
def step_impl(context):
    context.driver.close()