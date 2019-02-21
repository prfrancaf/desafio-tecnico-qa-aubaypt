from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def click(self, locator):
        self.wait_for(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        element = self.wait_for(EC.visibility_of_element_located(locator))
        return element

    def wait_for(self,condition, seconds = 5):
        return  WebDriverWait(self.driver,seconds).until(condition)

    def select_by_visible_text(self, locator, text):
        select = Select(self.find(locator))
        select.select_by_visible_text(text)

    def type_in(self,locator,text,set_clear = True):
        element = self.find(locator)
        if set_clear:
            element.clear()
        element.send_keys(text)
