import utilities.custom_logger as cl
import time
from traceback import print_stack


class Utils(object):
    log = cl.custom_logging()

    def verifyTextMatch(self, expectedText, actualText):
        self.log.info("Expected Text from the UI :" + "-" * 8 + "> " + expectedText)
        self.log.info("Actual Text from the UI :" + "-" * 8 + "> " + actualText)
        if expectedText == actualText:
            self.log.info("$"*8+"Text Matches"+"$"*8)
            return True
        else:
            self.log.error("#" * 8 + "Text Mis-Matches" + "#" * 8)
            return False

    def sleep(self,sec,info=''):
        self.log.info("Wait :: "+str(sec)+" seconds for "+info)
        try:
            time.sleep(sec)
        except InterruptedError:
            print_stack()

    def verifyTextContains(self, subText, superText):
        self.log.info("Expected Text from the UI :" + "-" * 8 + ">" + subText)
        self.log.info("Actual Text from the UI :" + "-" * 8 + ">" + superText)
        if subText in superText:
            self.log.info("$" * 8 + "Text Contains" + "$" * 8)
            return True
        else:
            self.log.error("#" * 8 + "Text does not Contains" + "#" * 8)
            return False