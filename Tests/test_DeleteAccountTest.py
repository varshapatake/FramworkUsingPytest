from lib.pageObjects.DeleteAccount import DeleteAccount1

def test_deleteaccount(option,launch_browser,database_connection):
    da=DeleteAccount1(launch_browser)
    da.deleteacc(option[9])
    with database_connection:
        database_connection.execute_query1("delete from newaccountinfo where accno=%d"%(option[9]))
    launch_browser.quit()


