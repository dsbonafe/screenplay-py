from behave import given
from core.webdriver import DriverFactory
from selenium.webdriver.chrome.options import Options

@given(u'I go to the homepage')
def given_i_am_here(context):
    driverOptions = Options()
    driverFactory = DriverFactory(driverOptions=driverOptions)
    driver = driverFactory.build()
    driver.get('http://www.google.com')