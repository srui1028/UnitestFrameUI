from selenium import webdriver
from time import sleep
from getDate import GetDate
from ddt import ddt,data
import unittest

@ddt
class Test_Login(unittest.TestCase):

    @data(GetDate().xlsx())
    def test_login(self,data):
        self.driver = webdriver.Chrome()
        self.driver.get("https://passport.ctrip.com/user/login?")
        sleep(3)
        self.driver.find_element_by_id('nloginname').send_keys(data[0]['username'])
        sleep(3)
        self.driver.find_element_by_id('npwd').send_keys(data[0]['passwd'])
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()