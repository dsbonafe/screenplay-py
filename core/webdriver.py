"""
In this module, we created a driver factory respecting the SOLID principles
"""

from selenium import webdriver
from abc import ABC, abstractmethod

# Driver factory which creates singleton WebDrivers dinamically, given browser name and Options
class DriverFactory:

    def __init__(self,
                 browserName='chrome',
                 driverOptions=None,
                 headless=False):
        self.browserName = browserName.lower()
        self.driverOptions = driverOptions
        self.headless = headless
        self.driver = None

    def build(self):
        if self.headless and not self.driver:
            self.driver = HeadlessDriverGenerator(self.browserName,
                                             self.driverOptions).driver
        elif not self.driver:
            self.driver = NormalDriverGenerator(self.browserName,
                                           self.driverOptions).driver
        return self.driver

# Abstract extensible class with the signature to create any kind of browser in the future
class Driver(ABC):

    @abstractmethod
    def driver(self):
        pass

# Creates a headless browser with Chrome as default
class HeadlessDriverGenerator(Driver):

    def __init__(self, browserName='chrome', options=None):
        self.browserName = browserName.lower()
        self.options = options
        self.options.add_argument('--headless')

    @property
    def driver(self):
        return NormalDriverGenerator(self.browserName, self.options)

# Creates a non-headless browser with Chrome as default
class NormalDriverGenerator(Driver):

    def __init__(self, browserName='chrome', options=None):
        self.browserName = browserName.lower()
        self.options = options
        self.__driver = None
        if not self.options:
            raise Exception('You must define the driver options before')

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if self.browserName == 'safari':
            self.__driver = webdriver.Safari(self.options)

        elif self.browserName == 'firefox':
            self.__driver = webdriver.Firefox(options=self.options)

        else:
            self.browserName == 'chrome'
            self.__driver = webdriver.Chrome(options=self.options)

    @property
    def driver(self):
        return self.__driver
