from lib.pageObjects.Withdrawal import Withdrawal1

def test_withdrawal(option,launch_browser,database_connection):
    w=Withdrawal1(launch_browser)
    balance=w.withdraw_check(option[1],1000,'withdraw')
    with database_connection:
        database_connection.execute_query1("update newaccountinfo set currentamount='%s' where accno=%d"%(balance,option[1]))
    launch_browser.quit()

