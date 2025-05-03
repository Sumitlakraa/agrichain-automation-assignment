from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_box = (By.ID, "inputBox")     
        self.submit_btn = (By.ID, "submitBtn")    

    def enter_text(self, text):
        self.driver.find_element(*self.input_box).send_keys(text)

    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()
