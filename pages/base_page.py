from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to(self, ele):
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()
