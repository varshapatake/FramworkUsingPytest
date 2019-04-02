import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from lib.DatabaseConnector.databseconnector import DatabaseConnection

@pytest.fixture(scope = 'module')
def base_url():
    return("http://demo.guru99.com/V4")

@pytest.fixture
def launch_browser(base_url):
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = False
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_url)

    username = driver.find_element(By.NAME, "uid")
    username.send_keys("mgr123")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("mgr!23")
    submit = driver.find_element(By.NAME, "btnLogin")
    submit.click()

    return driver

@pytest.fixture(scope='module')
def database_connection():
    yield DatabaseConnection()



def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default=[6,48748,'2018-08-31','2018-09-04',1000,5,14572,48748,7,48936],help="my option: 1090"
    )                                       #id,accno1,fdate,tdate,amount,noftransactions,newcustid,accno2,accno3

@pytest.fixture(scope='module')
def option(request):
    return request.config.getoption("--cmdopt")



import sys


def pytest_load_initial_conftests(args):
    if "xdist" in sys.modules:  # pytest-xdist plugin
        import multiprocessing

        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args


