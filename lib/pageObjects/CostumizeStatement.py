from selenium.webdriver.common.by import By


class CustumizeStatement1:
    def __init__(self,driver):
        self.driver=driver

    def custumize_state_check(self,accno,fdate,tdate,mtranvalue,noftran):
        self.driver.find_element(By.LINK_TEXT,"Customised Statement").click()
        title=self.driver.find_element(By.XPATH,"html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text

        assert(title=="Customized Statement Form")
        self.driver.find_element(By.NAME,"accountno").send_keys(accno)
        self.driver.find_element(By.NAME, "fdate").send_keys(fdate)
        self.driver.find_element(By.NAME, "tdate").send_keys(tdate)
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(mtranvalue)
        self.driver.find_element(By.NAME, "numtransaction").send_keys(noftran)
        self.driver.find_element(By.NAME,"AccSubmit").click()

        title1=self.driver.find_element(By.XPATH,"html/body/table/tbody/tr[1]/td/p").text
        assert(title1=="Transaction Details for Account No: 48748 from Date: 2018-08-31 to: 2018-09-04")
        assert(self.driver.find_element(By.XPATH,"html/body/table/tbody/tr[6]/td").is_displayed())
        print("pass")