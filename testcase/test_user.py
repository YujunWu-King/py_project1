import unittest
from selenium import webdriver
from wyj_po_practice.page.user import  *
from wyj_po_practice.page.login import *
class test_user(unittest.TestCase,user):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://tbsi.tranzvision.net:8082/login")
        self.driver.maximize_window()
    '''def tearDown(self):
        self.driver.quit()'''
    def login(self):
        ecp=login(self.driver)
        ecp.login_click('TBSI_Admin','123456')
        print("login")
    def in_usrmanage(self):
        print("haha")
        self.to_user()
    def test_add(self):
        self.login()
        time.sleep(20)
        self.in_usrmanage()
        time.sleep(10)
        self.added_user('zyzy')
        #self.add_user('zyzy','123456')




