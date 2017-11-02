from pages.blog_page import BlogPage
import unittest
import pytest
import utilities.custom_logger as cl
from selenium import webdriver

class TestBlogPage(unittest.TestCase):

    log = cl.custom_logging()

    baseUrl = 'https://rishubhatia.wixsite.com/website'
    # baseUrl = 'http://conscioustester.blogspot.com/'
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseUrl)

    #variable
    __comment = "Chikku-Test user likes to blog. The comment of the blog can be anything "
    __blog = "24 hours in Washington D.C."

    def setUp(self):
        self.bp = BlogPage(self.driver)

    @pytest.mark.run(order=1)
    def test_addComment(self):
        self.bp.enterText(blogLinkText=self.__blog,comment=self.__comment)
