from selenium.webdriver.common.by import By


class logout_page_locators:
    #Locators
    USER_BACK = (By.XPATH, "(//*[name()='image'])[1]")
    USER_LOGOUT = (By.XPATH, "//span[text()='Log Out']")

    def __init__(self, driver):
        self.driver = driver
    
    #Click on user profile
    def user_logout_profile(self):
        return self.driver.find_element(*logout_page_locators.USER_BACK).click()

    #Click on LOGOUT button
    def user_logout(self):
        return self.driver.find_element(*logout_page_locators.USER_LOGOUT).click()

