from selenium.webdriver.common.by import By
import time

class FundTransfer1:
    def __init__(self,driver):
        self.driver=driver

    def fundtransfer_check(self,accno1,accno2,amount,descrip):
        self.driver.find_element(By.LINK_TEXT,"Fund Transfer").click()
        self.driver.find_element(By.NAME, "payersaccount").send_keys(accno1)
        self.driver.find_element(By.NAME, "payeeaccount").send_keys(accno2)
        self.driver.find_element(By.NAME, "ammount").send_keys(amount)
        self.driver.find_element(By.NAME, "desc").send_keys(descrip)
        self.driver.find_element(By.NAME, "AccSubmit").click()

