from pages.home_page import HomePage
from selenium import webdriver
import unittest
import pytest
import utilities.custom_logger as cl
class TestHomePage(unittest.TestCase):
    log = cl.custom_logging()

    baseUrl = 'https://rishubhatia.wixsite.com/website'
    #baseUrl = 'http://conscioustester.blogspot.com/'
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseUrl)

    def setUp(self):
        self.hp = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_responeCode(self):
        self.log.info("Started Testing")
        self.hp.responseVerification()

    @pytest.mark.run(order=2)
    def test_brokenLinks(self):
        self.log.info("Verifying Broken Links")
        self.hp.listBrokenLinks()

    @pytest.mark.run(order=3)
    def test_title(self):
        self.hp.verifyTitle("SDET TEST")