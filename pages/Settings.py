from selenium.webdriver.common.by import By


class Setting_page_locators:
    SETTING_PRIVACY = (By.XPATH, "//span[text()='Settings & privacy']")
    SETTINGS = (By.XPATH, "//span[text()='Settings']")
    USER_EMAIL_ID = (By.XPATH, "//li[@data-testid='settings_section_email']//strong[contains(text(),'smilysurbhi@gmail.com')]")  #strong[text()='smilysurbhi@gmail.com'][@xpath="1"]
    USER_BLOCK = (By.XPATH, "//span[text()='Blocking']")
    USER_BLOCK_EDIT = (By.XPATH, "(//span[@class='b6ax4al1 lq84ybu9 hf30pyar om3e55n1 oshhggmv qm54mken'][normalize-space()='Edit'])[2]")
    USER_BLOCK_LIST = (By.XPATH, "(//span[text()='See your blocked list'])[1]")
    USER_BLOCK_LIST_COUNT = (By.XPATH, "//div[@class='h8391g91 m0cukt09 kpwa50dg ta68dy8c b6ax4al1']")
    USER_BLOCK_CLOSE = (By.XPATH, "//div[@aria-label = 'Close']/i[@class='gneimcpu oee9glnz']")

    def __init__(self, driver):
        self.driver = driver
    
    """Click on USER SETTING PRIVACY"""
    def user_settings_privacy(self):
        return self.driver.find_element(*Setting_page_locators.SETTING_PRIVACY).click()

    """"Click on SETTING"""
    def user_setting(self):
        return self.driver.find_element(*Setting_page_locators.SETTINGS).click()
    
    """"Switch to frame and fetch text from locator"""
    def user_email(self):
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])   
        return self.driver.find_element(*Setting_page_locators.USER_EMAIL_ID).text
    """"Close frame"""
    def close_iframe(self):
        self.driver.switch_to.default_content()
    
    """"Click on block"""
    def user_block(self):
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK).click()
    
    """"Click on user block edit"""
    def user_block_edit(self):
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK_EDIT).click()
    
    """"Click on block list"""
    def user_block_list(self):
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK_LIST).click()
    
    """"Count no. of blocked user from list"""
    def user_block_list_count(self):
        count = self.driver.find_elements(*Setting_page_locators.USER_BLOCK_LIST_COUNT)
        return len(count)
    
    """"Close block window"""
    def user_block_close(self):
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK_CLOSE).click()
    


    


























        # driver = self.Homepage_locators()
        # # Name = driver.find_element(By.XPATH, "//strong[text()='Surbhi Agrahari']").text()
        # Name = driver.find_element(By.XPATH, "//strong[@xpath='1']").text
        # print(Name)
        # return Name
        # # time.sleep(4)
        # # username = driver.find_element(By.XPATH, "//strong[text()=' https://www.facebook.com/']").text
        # # print(username)
        # # # time.sleep(4)
        # # contact = driver.find_element(By.XPATH, "//span[text()='Primary: ']").text
        # # print(contact)

# obj = Setting_page_locators()
# # obj.test_chrome()
# # obj.username_locators()
# obj.Settingpage_locators()
