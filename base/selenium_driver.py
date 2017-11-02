from selenium import webdriver
import logging
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack


class SeleniumDriver:
    log = cl.custom_logging(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        else:
            self.log.info("Locator Type " + locatorType + " not supported")
            return False

    def getElement(self, locator,locatorType='xpath',element = None):

        try:

            byType = self.getType(locatorType=locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element found with locator: " + locator + " locatorType: " + locatorType.title())
        except:
            self.log.info("Element not found with locator: " + locator + " locatorType: " + locatorType.title())

        return element

    def responseVerification(self):
        res = requests.get(url=self.driver.current_url)
        self.log.info("Response of the URL : {} is : {}".format(self.driver.current_url, res))

    def getTitle(self):
        return self.driver.title

    def clickElement(self, locator='',locatorType='',element=None):
        if element is None:
            element = self.getElement(locator=locator,locatorType=locatorType)

        self.log.info("Clicking on the element : {}".format(element))
        element.click()

    def sendKeys(self, data, locator='', locatorType='xpath', element=None):
        if element is None:
            element = self.getElement(locator=locator,locatorType=locatorType)

        self.log.info("Entering text : {} to the element : {}".format(data,element))
        element.clear()
        element.send_keys(data)
        self.log.info('Entered "{}" at element with locator: "{}" locatorType: "{}"'.format(data,locator,locatorType))

    def waitForElement(self, locator, locatorType='xpath', timeout=10, pollfrequency=0.5, element=None):
        try:
            byType = self.getType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element : {} to be clickable".format(locator))
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollfrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotSelectableException,
                                                     ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable(byType, locator))
            self.log.info("Element {} appeared on the website ".format(element))
        except:
            self.log.error("Element not appeared after waiting {} seconds".format(timeout))
            print_stack()

        return element

    def getElementAttr(self,element,attr):
        self.log.info("Getting attribute : for element : {}".format(attr,element))
        return element.get_attribute(attr)
