from lib.pageObjects.FundTransfer import FundTransfer1

def test_fund_transfer(option,launch_browser,database_connection):
    ft=FundTransfer1(launch_browser)
    ft.fundtransfer_check(option[1],option[7],1000,'trasfering')

    with database_connection:
        balance1=database_connection.execute_query2("select currentamount from newaccountinfo where accno=%d"%(option[1]))[0]
        balance2 = database_connection.execute_query2("select currentamount from newaccountinfo where accno=%d" % (option[7]))[0]
        balance1=int(balance1[0])-1000
        balance1=str(balance1)
        balance2 = int(balance2[0]) + 1000
        balance2 = str(balance2)
        database_connection.execute_query1("update newaccountinfo set currentamount='%s' where accno=%d"%(balance1,option[1]))
        database_connection.execute_query1("update newaccountinfo set currentamount='%s' where accno=%d"%(balance2,option[7]))
    launch_browser.quit()





