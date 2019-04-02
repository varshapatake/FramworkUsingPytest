from selenium.webdriver.common.by import By
class EditAccount:
    def __init__(self,driver):
        self.driver=driver

    def editaccount(self,accno,database_connection):
        editaccount=self.driver.find_element(By.XPATH,"html/body/div[3]/div/ul/li[6]/a")   #inserting data in editaccount form
        editaccount.click()
        acc=self.driver.find_element(By.NAME,"accountno")
        acc.send_keys(accno)
        submit=self.driver.find_element(By.NAME,"AccSubmit")
        submit.click()
        select = self.driver.find_element(By.NAME,"a_type")
        select.click()
        accountt = database_connection.execute_query2("select acctype from newaccountinfo where accno=%d" % (accno))[0]

        if (accountt[0] == 'Current'):
            self.driver.find_element(By.XPATH,"html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/select/option[2]").click()
        else:
            self.driver.find_element(By.XPATH,"html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/select/option[1]").click()

        submit1=self.driver.find_element(By.NAME, "AccSubmit")
        submit1.click()
        submit1.click()
        acctype=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[8]/td[2]").text
        return acctype





    




