from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from lib.pageObjects.login import login
import time
class Logout:
    def __init__(self,driver):
        self.driver = driver


    def logout(self):
        logout=self.driver.find_element(By.XPATH,"html/body/div[3]/div/ul/li[15]/a")
        logout.click()
        try:
            self.driver.switch_to.alert.accept()
            print('Alert occur')
        except NoAlertPresentException:
            print('No alter present')
        time.sleep(3)

        self.driver.close()

