from lib.pageObjects.Deposite import Deposite1

def test_deposite(option,launch_browser,database_connection):
    d=Deposite1(launch_browser)
    balance=d.deposite_check(option[1],10000,'depositing')

    with database_connection:
        database_connection.execute_query1("update newaccountinfo set currentamount='%s' where accno=%d"%(balance,option[1]))

    launch_browser.quit()