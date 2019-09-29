from selenium.webdriver.common.by import By
import time
from wyj_po_practice.base.basepage import WebDriver
class login(WebDriver):
    schxiala_locate=(By.ID,'combo-1010-trigger-picker')
    school_locate=(By.XPATH,'//div[@id="boundlist-1017-listWrap"]/ul/li[3]')
    username_locate=(By.ID,'textfield-1011-inputEl')
    password_locate=(By.ID,'textfield-1012-inputEl')
    login_button=(By.ID,'btSubmit-btnEl')
    error_text=(By.XPATH,'//div[@id="box-1015"]/div')
    @property
    def school(self):
        #dd=self.findElement(*self.schxiala_locate)
        self.findElement(*self.schxiala_locate).click()
        time.sleep(5)
        #cc=self.findElement(*self.school_locate)
        self.findElement(*self.school_locate).click()

    def username(self,usr):
        #dd=self.findElement(*self.username_locate)
        self.findElement(*self.username_locate).send_keys(usr)

    def password(self,pwd):
        self.findElement(*self.password_locate).send_keys(pwd)

    def click(self):
        #ee=self.findElement(*self.login_button)
        self.findElement(*self.login_button).click()
    @property
    def get_errortxt(self):
        return self.findElement(*self.error_text).text

    def login_click(self,usr,pwd):
        self.school
        self.username(usr)
        self.password(pwd)
        time.sleep(15)
        self.click()
        print("点击登录")