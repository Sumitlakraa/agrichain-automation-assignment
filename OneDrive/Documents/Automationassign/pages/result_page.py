from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_text = (By.ID, "resultText")

    def get_output(self):
        return self.driver.find_element(*self.result_text).text
