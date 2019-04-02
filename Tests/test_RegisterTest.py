import time
from lib.pageObjects.registration import Registration

def test_register(option,launch_browser, database_connection):

    lp = Registration(launch_browser)

    with database_connection:
        customer= database_connection.execute_query2("select * from customer where id = %d" % (option[0]))
        print(customer)
        customer1=customer[0]
        print(customer1)


        usernewid = lp.register_to_website(customer1[0], customer1[1], customer1[2], customer1[3], customer1[4],
                                           customer1[5],
                                           customer1[6], customer1[7], customer1[10], customer1[8])
        usernewid = int(usernewid)

        query = "insert into registered_user(newid,Name,Gender,Dob,Address,City,State,pin,mobile,email,password) values(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            usernewid, customer1[0], customer1[1], customer1[2], customer1[3], customer1[4], customer1[5], customer1[6],
            customer1[7], customer1[10], customer1[8])



        database_connection.execute_query1(query)
        database_connection.execute_query1("delete from customer where id=%d" % (option[0]))
        time.sleep(4)
    launch_browser.quit()











