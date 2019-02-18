from behave import Given, When, Then, Step, use_step_matcher
from selenium import webdriver
import time
use_step_matcher("re")

@Step("I want to login baidu website")
def step_impl(context):
    context.BaiDuPage.access_baidu()


@Step("I want to enter (?P<value>.+) in search field")
def step_impl(context, value):
    context.BaiDuPage.input_value(value)


@Step("I want to click search button")
def step_impl(context):
    context.BaiDuPage.click_search_btn()


@Step("I want to stop test and close browser")
def step_impl(context):
    context.driver.close()