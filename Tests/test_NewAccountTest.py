from lib.pageObjects.newaccount import NewAccount

def testnewAccount(option,launch_browser,database_connection):
    with database_connection:
        na = NewAccount(launch_browser)
        deposite = database_connection.execute_query2("select InitialDeposite from account")[0]

        na.newaccount(option[6], deposite[0],database_connection)
        launch_browser.quit()
