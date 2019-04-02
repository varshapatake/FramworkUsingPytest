from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class DeleteAccount1:
    def __init__(self,driver):
        self.driver=driver


    def deleteacc(self,accno):
        self.driver.find_element(By.LINK_TEXT,"Delete Account").click()
        self.driver.find_element(By.NAME,"accountno").send_keys(accno)
        self.driver.find_element(By.NAME,"AccSubmit").click()

        try:
            self.driver.switch_to.alert.accept()
            print("alert accepted")
        except NoAlertPresentException:
            print("no alert occur")

        try:
            self.driver.switch_to.alert.accept()
            print("alert accepted")
        except NoAlertPresentException:
            print("no alert occur")



