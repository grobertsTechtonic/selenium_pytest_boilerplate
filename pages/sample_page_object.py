from .base_page import BasePage
from elements import SamplePageElements


class SamplePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.elements = SamplePageElements(driver)
