from selenium.webdriver.common.by import By

class Home_page_locators:

    USER_PROFILE = (By.XPATH, "(//*[name()='image'])[1]")
    PROFILE_NAME = (By.XPATH, "//span[@class='b6ax4al1 lq84ybu9 hf30pyar om3e55n1'][starts-with(text(),'Surbhi Agrahari')]")

    def __init__(self, driver):
        self.driver = driver
    
    """"Fetch text from locator"""
    def user_name(self):
        user = self.driver.find_element(*Home_page_locators.PROFILE_NAME).text
        return user
    
    """"Click on User Profile"""
    def user_profile(self):
        return self.driver.find_element(*Home_page_locators.USER_PROFILE).click()

