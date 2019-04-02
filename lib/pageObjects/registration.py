
from selenium.webdriver.common.by import By

class Registration:
    def __init__(self,driver):
         self.driver = driver

    def register_to_website(self,fname,Gender,dob,address,city ,state ,pinno ,telephone ,email ,password):

        newuser=self.driver.find_element(By.XPATH,"html/body/div[3]/div/ul/li[2]/a")
        newuser.click()
        regis=self.driver.find_element(By.XPATH,"html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p").text
        assert(regis=='Add New Customer')

        ufirstname = self.driver.find_element(By.NAME,"name")
        ufirstname.send_keys(fname)

        male=self.driver.find_element(By.XPATH,"html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")
        female=self.driver.find_element(By.XPATH,"html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")

        if(Gender =='Female'):
            female.click()
        else:
            male.click()

        ddob = self.driver.find_element(By.NAME, "dob")
        ddob.send_keys(dob)

        aadd = self.driver.find_element(By.NAME, "addr")
        aadd.send_keys(address)

        ccity = self.driver.find_element(By.NAME, "city")
        ccity.send_keys(city)

        sstate = self.driver.find_element(By.NAME, "state")
        sstate.send_keys(state)

        ppinno= self.driver.find_element(By.NAME, "pinno")
        ppinno.send_keys(pinno)

        ttelephoneno = self.driver.find_element(By.NAME, "telephoneno")
        ttelephoneno.send_keys(telephone)

        eemailid= self.driver.find_element(By.NAME, "emailid")
        eemailid.send_keys(email)

        ppassword = self.driver.find_element(By.NAME, "password")
        ppassword.send_keys(password)

        submit = self.driver.find_element(By.NAME, "sub")
        submit.click()

        success=self.driver.find_element(By.XPATH,".//*[@id='customer']/tbody/tr[1]/td/p").text
        assert(success=="Customer Registered Successfully!!!")

        usernewid = self.driver.find_element(By.XPATH, ".//*[@id='customer']/tbody/tr[4]/td[2]")
        usernewid = usernewid.text

        return usernewid







