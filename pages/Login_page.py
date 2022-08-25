from selenium.webdriver.common.by import By


class login_page_locators:
    #Locators
    EMAIL_ID = (By.XPATH, "//input[@type='text']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT = (By.NAME, "login")

    def __init__(self, driver, user_params):
        self.driver = driver
        # self.user_email = user_email
        # self.user_password = user_password
        self.user_params = user_params

    
    #Enter EMAIL
    def username(self):
        # return self.driver.find_element(*login_page_locators.EMAIL_ID).send_keys("smilysurbhi@gmail.com")
        return self.driver.find_element(*login_page_locators.EMAIL_ID).send_keys(self.user_params["user_email"])


    #Enter PASSWORD
    def password(self):
        # return self.driver.find_element(*login_page_locators.PASSWORD).send_keys("80bandana90")
        return self.driver.find_element(*login_page_locators.PASSWORD).send_keys(self.user_params["user_password"])

    #Click SUBMIT
    def submit_button(self):
        return self.driver.find_element(*login_page_locators.SUBMIT).click()
