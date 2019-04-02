from selenium.webdriver.common.by import By
from lib.DatabaseConnector.databseconnector import DatabaseConnection
class NewAccount:
    def __init__(self,driver):
        self.driver=driver



    def newaccount(self,custid,ideposite,database_connection):

        naccount=self.driver.find_element(By.XPATH,"html/body/div[3]/div/ul/li[5]/a")
        naccount.click()

        customerid=self.driver.find_element(By.NAME,"cusid")
        customerid.send_keys(custid)

        select=self.driver.find_element(By.NAME,"selaccount")
        select.click()
        select1 = self.driver.find_element(By.XPATH, "html/body/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[2]")
        select1.click()

        initdeposite = self.driver.find_element(By.NAME, "inideposit")
        initdeposite.send_keys(ideposite)

        submit=self.driver.find_element(By.NAME,"button2")
        submit.click()



#getting new account info here

        accno=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[4]/td[2]")
        accno=accno.text
        accno=int(accno)

        custid=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[5]/td[2]")
        custid=custid.text
        custid=int(custid)

        custname=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[6]/td[2]")
        custname=custname.text

        email=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[7]/td[2]")
        email=email.text

        acctype=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[8]/td[2]")
        acctype=acctype.text

        dateofopen=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[9]/td[2]")
        dateofopen=dateofopen.text

        currentamm=self.driver.find_element(By.XPATH,".//*[@id='account']/tbody/tr[10]/td[2]")
        currentamm=currentamm.text


#saving new account info in database
        with database_connection:

            database_connection.execute_query1("insert into newaccountinfo(accno,custid,custname,email,acctype,dateofopen,currentamount)values(%d,%d,'%s','%s','%s','%s','%s')"%(accno,custid,custname,email,acctype,dateofopen,currentamm))








