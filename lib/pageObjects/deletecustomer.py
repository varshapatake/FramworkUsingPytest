from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

class DeleteCustomer:
    def __init__(self,driver):
        self.driver=driver

    def deletecustomer(self,newid):
        delete=self.driver.find_element(By.XPATH,"html/body/div[3]/div/ul/li[4]/a")
        delete.click()
        userid=self.driver.find_element(By.NAME,"cusid")
        userid.send_keys(newid)
        submit=self.driver.find_element(By.NAME,"AccSubmit")
        submit.click()

        try:
            self.driver.switch_to.alert.accept()
            print("alert accepted")
        except NoAlertPresentException:
            print('No alter present')

        time.sleep(3)



