
from lib.pageObjects.deletecustomer import DeleteCustomer
import pytest

@pytest.mark.parametrize("id",
    [897,
    ])
def test_deletecustomer(id,launch_browser,database_connection):
    with database_connection:
        dc = DeleteCustomer(launch_browser)
        dc.deletecustomer(id)
        print("customer deleted successfully")
        result = database_connection.execute_query2("select Name,Gender,Dob,email from registered_user where newid=%d" % (id))[0]
        database_connection.execute_query1("delete from registered_user where newid=%d" % (id))
        query = "insert into deleted_user(id,Name,Gender,Dob,email) values(%d,'%s','%s','%s','%s')" % (
        id, result[0], result[1], result[2], result[3])
        database_connection.execute_query1(query)
        launch_browser.quit()

