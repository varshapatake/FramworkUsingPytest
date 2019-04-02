from lib.pageObjects.CostumizeStatement import CustumizeStatement1

def test_custum_state(option,launch_browser):
    cs=CustumizeStatement1(launch_browser)
    cs.custumize_state_check(option[1],option[2],option[3],option[4],option[5])
    launch_browser.quit()

