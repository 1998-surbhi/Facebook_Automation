import inspect
import logging
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driver_setup", "passing_username_password")
class BasePage:

    def wait_clickable(self, path):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.element_to_be_clickable((path)))
        except Exception as e:
            self.message_logging(e)
    
    def message_logging(self, message):
        """"
        Create Log File
        """
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("/home/cbnits/Documents/Facebook_Assignment/Log/logfile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)
