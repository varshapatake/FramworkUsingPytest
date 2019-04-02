from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

class Editcustomer:
    def __init__(self,driver):
        self.driver = driver

    def editcustomer(self,id,address,city,state,pinno,telephone,email):
        editcustomer=self.driver.find_element(By.XPATH,"html/body/div[3]/div/ul/li[3]/a")
        editcustomer.click()
        custid=self.driver.find_element(By.NAME,"cusid")
        custid.send_keys(id)
        submit = self.driver.find_element(By.NAME, "AccSubmit")
        submit.click()
        aadd = self.driver.find_element(By.NAME, "addr")
        aadd.clear()
        aadd.send_keys(address)
        ccity = self.driver.find_element(By.NAME, "city")
        ccity.clear()
        ccity.send_keys(city)
        sstate = self.driver.find_element(By.NAME, "state")
        sstate.clear()
        sstate.send_keys(state)
        ppinno = self.driver.find_element(By.NAME, "pinno")
        ppinno.clear()
        ppinno.send_keys(pinno)
        ttelephoneno = self.driver.find_element(By.NAME, "telephoneno")
        ttelephoneno.clear()
        ttelephoneno.send_keys(telephone)
        eemailid = self.driver.find_element(By.NAME, "emailid")
        eemailid.clear()
        eemailid.send_keys(email)
        submit = self.driver.find_element(By.NAME, "sub")
        submit.click()

        try:
            self.driver.switch_to.alert.accept()
            print("alert accepted")
        except NoAlertPresentException:
            print('No alter present')






