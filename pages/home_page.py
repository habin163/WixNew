from selenium import webdriver
import requests
import utilities.broken_link_list as bl
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from utilities.utils import Utils


class HomePage(SeleniumDriver):
    log = cl.custom_logging()

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.utils = Utils()


    def listBrokenLinks(self):
        self.log.info("Verifying Broken Links "+"&"*10)
        bl.brokenLinkCheck(self.driver)

    def verifyTitle(self,expectedTitle):
        actualTitle = self.getTitle()
        self.utils.verifyTextMatch(expectedTitle,actualTitle)