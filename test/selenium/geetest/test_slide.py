from selenium import webdriver

from selenium.webdriver.common.by import By
from minitools.selenium.geetest import SlideSelenium
from selenium.webdriver.support import expected_conditions as EC

"""
BiLiBiLi: 模拟登陆
https://passport.bilibili.com/login
"""


class BiliBiliLogin(SlideSelenium):
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get("https://passport.bilibili.com/login")
        self.init_property()

    def capture_interface(self):
        username = self.waiter.until(EC.element_to_be_clickable((By.ID, 'login-username')))
        passwd = self.waiter.until(EC.element_to_be_clickable((By.ID, 'login-passwd')))
        button = self.waiter.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn btn-login"]')))
        username.clear()
        passwd.clear()
        username.send_keys(self.account)
        self.sleep(0.3)
        passwd.send_keys(self.password)
        self.sleep(2)
        button.click()

    def run(self):
        super(BiliBiliLogin, self).run()


if __name__ == '__main__':
    account = 'test'
    password = 'test'
    test = BiliBiliLogin(account, password)
    test.run()
