from selenium.webdriver.common.by import By


class SamplePageElements:
    def __init__(self, driver):
        self.driver = driver

    # define functions to return webelements using the by selector
    def sample_element(self):
        return self.driver.find_element(By.XPATH, '//input[@name=\'q\']')
