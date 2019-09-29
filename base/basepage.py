from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium import webdriver


class WebDriver(object):
    def __init__(self,driver):
        self.driver=driver
    def findElement(self,*loc):
        try:
            return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
            #return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findElements(self,*loc):
        try:
            return WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*loc))
            #return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def current_title(self):
        return self.driver.title