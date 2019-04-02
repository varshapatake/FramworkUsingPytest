
from lib.pageObjects.editaccount import EditAccount

def test_editaccount(option,launch_browser,database_connection):
    with database_connection:
        ea = EditAccount(launch_browser)
        acctype2 = ea.editaccount(option[1],database_connection)
        print(acctype2)

        database_connection.execute_query1("update newaccountinfo set acctype='%s' where accno=%d"%(acctype2,option[1]))
        launch_browser.quit()



