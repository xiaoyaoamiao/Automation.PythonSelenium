# -*- coding: utf8 -*-
from selenium import webdriver
from baidu_page import BaiDuPage
import time
stored_feature_name = ''
stored_scenario_name = ''

def before_all(context):
    context.driver = webdriver.Chrome(executable_path='/Users/miaog001/Documents/AutoProjects/chromedriver')
    context.BaiDuPage = BaiDuPage(context)

def before_feature(context, feature):
    global stored_feature_name
    stored_feature_name = feature.name
    print(stored_feature_name)


def before_scenario(context, scenario):
    global stored_scenario_name
    stored_scenario_name = scenario.name


def after_feature(context, feature):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_all(context):
    context.driver.close()