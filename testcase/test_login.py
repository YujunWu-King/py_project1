from selenium import webdriver
import unittest
from wyj_po_practice.page.login import  *


class test_login(unittest.TestCase,login):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://tbsi.tranzvision.net:8082/login')
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test01(self):
        self.login_click('TBSI_Admin','123456')
        text=self.get_errortxt
        self.assertIn(text,' 登录信息未填写完整')
