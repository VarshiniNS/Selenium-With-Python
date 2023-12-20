import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def explictwaitforPresence(self,Text):
        waitObject=WebDriverWait(self.driver,15)
        waitObject.until(EC.presence_of_element_located((By.LINK_TEXT,Text)))

    def selectByText(self,locator,text):
        selectobj=Select(locator)
        selectobj.select_by_visible_text(text)
    def getlogger(self_):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        fileHandler= logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler) #file handler object
        logger.setLevel(logging.DEBUG)
        return logger