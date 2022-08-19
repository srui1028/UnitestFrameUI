'''
    index_page页面对象，实现搜索
'''
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from time import sleep
from selenium import webdriver
from page_object.login_page import LoginPage

class IndexPage(BasePage):
    # 元素定位
    url = "http://10.20.17.211:30000/"
    click_COE = (By.XPATH,"//span[contains(.,'卓越中心')]")
    search_input = (By.ID,"basic_name")
    click_select = (By.XPATH,"//span[contains(.,'查 询')]")

    # 核心业务流
    def select(self,txt):
        self.visit()
        self.click(self.click_COE)
        sleep(2)
        self.input(self.search_input,txt)
        self.click(self.click_select)
        sleep(2)




if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = "admin"
    pwd = "admin"
    txt = "55"
    sec = IndexPage(driver)
    sec.select(txt)
    lp = LoginPage(driver)
    lp.login(user, pwd)









