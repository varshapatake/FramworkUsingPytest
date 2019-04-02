from selenium.webdriver.common.by import By


class MiniStatement1:
    def __init__(self,driver):
        self.driver=driver

    def mini_state_check(self,accno):
        self.driver.find_element(By.LINK_TEXT,"Mini Statement").click()
        title= self.driver.find_element(By.XPATH,"html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text
        assert(title=='Mini Statement Form')
        self.driver.find_element(By.NAME,"accountno").send_keys(accno)
        self.driver.find_element(By.NAME,"AccSubmit").click()
        tran=self.driver.find_element(By.XPATH,"html / body / table / tbody / tr[1] / td / p").text
        assert(tran=="Last Five Transaction Details for Account No: 48748")
        minitable=self.driver.find_element(By.XPATH, "html/body/table/tbody/tr[2]/td")
        assert(minitable.is_displayed())
        print("pass")
