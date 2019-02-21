from os.path import dirname, realpath

from selenium import webdriver

def before_all(context):
    context.base_url = context.config.userdata['BASE_URL']

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(executable_path=dirname(realpath(__file__)) + "/resources/chromedriver")
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.close()
