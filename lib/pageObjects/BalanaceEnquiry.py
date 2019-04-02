from selenium.webdriver.common.by import By


class BalanceEnquiry1:
    def __init__(self,driver):
        self.driver=driver

    def balance_check(self,accno):
        self.driver.find_element(By.LINK_TEXT,"Balance Enquiry").click()
        self.driver.find_element(By.NAME,"accountno").send_keys(accno)
        self.driver.find_element(By.NAME, "AccSubmit").click()

        balance=self.driver.find_element(By.XPATH,".//*[@id='balenquiry']/tbody/tr[16]/td[2]").text
        return balance

