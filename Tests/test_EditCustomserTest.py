
from lib.pageObjects.editcustomer import Editcustomer
import pytest


def test_register(option,launch_browser,database_connection):

    with database_connection:
        lp = Editcustomer(launch_browser)
        lp.editcustomer(option[6], "ravi dhgjhgh nagar ", "wewghfhhgtryf", "fgggkjjkyhhgj", "455789", "45768997566",
                        "rekhaaddiiii556@gmail.com")

        database_connection.execute_query1("UPDATE registered_user SET Address = 'ravi dhgjhgh nagar', City='wewghfhhgtryf' ,State='fgggkjjkyhhgj',pin='455789',mobile='45768997566', email='rekhaaddiiii556@gmail.com' WHERE newid=%d"%(option[6]))

        launch_browser.quit()

