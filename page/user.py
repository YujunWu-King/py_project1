from selenium.webdriver.common.by import By
import time
from wyj_po_practice.base.basepage import WebDriver
class user(WebDriver):
    #to_user 的 UI
    to_click=(By.ID,'tool-1012')
    #main_menu=(By.ID,'tool-1042-toolEl')
    query_menu=(By.ID,'textfield-1045-inputEl')
    #menu_click=(By.ID,'textfield-1039-trigger-search')
    usrmanage_click=(By.XPATH,'//*[@id="treeview-1044-record-47"]/tbody/tr/td/div')
    #add_user 的 UI
    add_button=(By.ID,'button-1080-btnInnerEl')
    add_username=(By.NAME,'usAccNum')
    add_password=(By.NAME,'password')
    add_qrpassword=(By.NAME,'reptPassword')
    add_click=(By.ID,'button-1140-btnInnerEl')
    #add_quit=(By.ID,'button-1252-btnInnerEl')
    #username_list
    all_user=(By.XPATH,'//*[@id="gridview-1272"]/div[2]/table/tbody/tr/td[3]')
    all_pages=(By.ID,'tbtext-1097')

    #query_user 的UI
    query_button=(By.ID,'button-1078-btnInnerEl')
    query_username=(By.NAME,'TZ_DLZH_ID-value')
    query_click=(By.XPATH,'//span[contains(text(),"搜索")]')
    query_text=(By.XPATH,'/html/body/div[3]/div[4]/div[2]/div[3]/div[1]/div[2]/table/tbody/tr/td[3]/div')
    #del_user 的UI
    select_user=(By.CLASS_NAME,'x-grid-row-checker')
    del_button=(By.ID,'button-1285-btnEl')
    del_click=(By.ID,'button-1006-btnInnerEl')

    def to_user(self):
        print("执行了吗")
        self.findElement(*self.to_click).click()
        print(self.findElement(*self.to_click))
        #self.findElement(*self.main_menu).click()
        print("zhxingle")
        time.sleep(20)
        self.findElement(*self.query_menu).send_keys('用户')
        time.sleep(20)
        #self.findElement(*self.menu_click).click()
        self.findElement(*self.usrmanage_click).click()


    def add_user(self,new_usr,new_pwd):
        self.findElement(*self.add_button).click()
        self.findElement(*self.add_username).send_keys(new_usr)
        self.findElement(*self.add_password).send_keys(new_pwd)
        self.findElement(*self.add_qrpassword).send_keys(new_pwd)
        time.sleep(20)
        self.findElement(*self.add_click).click()
        #self.findElement(*self.add_quit).click()

    def query_user(self,new_usr):
        self.findElement(*self.query_button).click()
        self.findElement(*self.query_username).send_keys(new_usr)
        self.findElement(*self.query_click).click()
    #获取查询结果的账号名
    @property
    def get_queryResult(self):
         return self.findElement(*self.query_text).text

    def del_user(self):

        print(self.findElements(*self.select_user))
        self.findElement(*self.del_button).click()
        self.findElement(*self.del_click).click()

#遍历获取列表中所有的登录账号-8
    def added_user(self,new_usr):

        self.findElement(*self.query_button).click()
        time.sleep(5)
        self.findElement(*self.query_username).send_keys(new_usr)
        time.sleep(5)
        self.findElement(*self.query_click).click()
        time.sleep(5)
        print("+++++++++++")
        print(self.get_queryResult)
        if  self.get_queryResult==new_usr:
            time.sleep(5)
            self.del_user()
        else:
            self.add_user('zyzy', '123456')







