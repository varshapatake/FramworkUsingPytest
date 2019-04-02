
from lib.pageObjects.logout import Logout
def test_logot(launch_browser):
    lp = Logout(launch_browser)
    lp.logout()




