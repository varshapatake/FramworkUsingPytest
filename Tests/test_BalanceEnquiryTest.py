from lib.pageObjects.BalanaceEnquiry import BalanceEnquiry1

def test_balance_enquiry(option,launch_browser,database_connection):
    be=BalanceEnquiry1(launch_browser)
    balance=be.balance_check(option[1])
    with database_connection:
        currentbalance=database_connection.execute_query2("select currentamount from newaccountinfo where accno=%d"%(option[1]))[0]
        assert (currentbalance[0]==balance)
        print(balance)

    launch_browser.quit()



