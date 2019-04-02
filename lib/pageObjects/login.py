
from selenium.webdriver.common.by import By


class login:
    def __init__(self,driver):
        self.driver = driver


    # def login(self,name,pwd):
    #     username = self.driver.find_element(By.NAME, "uid")
    #     username.send_keys(name)
    #
    #
    #     password = self.driver.find_element(By.NAME, "password")
    #     password.send_keys(pwd)
    #
    #     submit = self.driver.find_element(By.NAME, "btnLogin")
    #     submit.click()
    #
    #     self.driver.close()


