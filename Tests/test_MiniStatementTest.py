from lib.pageObjects.MiniStatement import MiniStatement1

def test_mini_statement(option,launch_browser) :#option represent array of diff arguments
    ms=MiniStatement1(launch_browser)
    ms.mini_state_check(option[1]) #option[1] contain accno
    launch_browser.quit()
