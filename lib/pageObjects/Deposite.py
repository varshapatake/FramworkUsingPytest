from selenium.webdriver.common.by import By


class Deposite1:
    def __init__(self,driver):
        self.driver=driver

    def deposite_check(self,accno,ammount,descrip):
        self.driver.find_element(By.LINK_TEXT,"Deposit").click()
        self.driver.find_element(By.NAME,"accountno").send_keys(accno)
        self.driver.find_element(By.NAME,"ammount").send_keys(ammount)
        self.driver.find_element(By.NAME,"desc").send_keys(descrip)
        self.driver.find_element(By.NAME,"AccSubmit").click()

        balance=self.driver.find_element(By.XPATH,".//*[@id='deposit']/tbody/tr[23]/td[2]").text
        return balance


