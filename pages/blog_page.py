from pages.home_page import HomePage
import utilities.custom_logger as cl
from utilities.utils import Utils
from selenium.webdriver.common.keys import Keys
import time


class BlogPage(HomePage):
    log = cl.custom_logging()

    # variables
    __iframe = "fb_ltr"
    __textAreaComment = './/textarea'
    __fbLoginButton = ".//button[contains(.,'Log In to Post')]/../.."
    __emailId = 'email'
    __upass = 'pass'
    __username = ''
    __password = ''
    __submit = 'login'
    __postButton = ".//button[contains(text(),'Post')]"
    __loadMoreComments = ".//button[contains(.,'Load 10 more')]"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.utils = Utils()

    def navigateToBlog(self, linkText):
        element = self.getElement(locator=linkText,locatorType='link')
        hiddenUrl = self.getElementAttr(element=element,attr='href')
        self.driver.get(hiddenUrl)
        self.utils.sleep(5,"Waiting for new page to load")

    def enterText(self,blogLinkText, comment=None, reply=None):
        self.navigateToBlog(blogLinkText)
        if comment:
            self.log.info("Performing comment to the blog")
            self.enterComment(comment)
        elif reply:
            self.log.info("Performing reply to a comment")
            self.eneterReply()
        else:
            self.log.error("Invalid kind of entering text to blog")

    def enterComment(self, data):
        try:
            parentWindow = self.driver.current_window_handle
            self.driver.execute_script("window.scrollBy(0,600);")
            self.utils.sleep(10,"Waiting for the frame element to get fully loaded")
            frameElement = self.getElement(locator=self.__iframe,locatorType='class')
            self.driver.switch_to.frame(frameElement)
            textAreaElement = self.getElement(locator=self.__textAreaComment)
            self.sendKeys(data=data, element=textAreaElement)
            self.utils.sleep(8,"Waiting  for Log In to Post button to appear")
            # self.driver.switch_to.window(parentWindow)
            self.log.info("Switching from window : {} to frame :{}".format(parentWindow,self.__iframe))
            # self.driver.switch_to.frame(frameElement)
            self.clickElement(locator=self.__loadMoreComments,locatorType='xpath')
            loginToPostButton = self.getElement(locator=self.__fbLoginButton)
            self.clickElement(element=loginToPostButton,locatorType='name')
            self.fbLoginPopup()
            self.driver.switch_to.frame(frameElement)
            # self.clickElement(locator=self.__loadMoreComments, locatorType='xpath')
            # return True
        except:
            self.log.error("Failed to enter comment")
            # return False

    def fbLoginPopup(self):

        parentHandle = self.driver.current_window_handle
        self.utils.sleep(5,"Waiting for the handlers to show up")
        handles = self.driver.window_handles

        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                submitButton = self.waitForElement(locator=self.__submit,locatorType='name')
                self.log.info("Facebook Popup Displayed and accessed ")
                self.sendKeys(data=self.__username,locator=self.__emailId,locatorType='id')
                self.sendKeys(data=self.__password,locator=self.__upass,locatorType='id')
                self.clickElement(locator=self.__submit,locatorType='name')



            else:
                self.log.error("Facebook popup not accessible")
                self.log.info("Switching back to parent window : {}".format(parentHandle))
            self.driver.switch_to.window(parentHandle)
            postButton = self.waitForElement(locator=self.__postButton)
            self.clickElement(element=postButton)

    def eneterReply(self):
        return True

    # def addComment(self,data):
