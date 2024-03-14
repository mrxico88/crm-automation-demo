from Browser import Browser
import os
import yaml
from Browser import ElementState
browser = Browser()


class BaseObject:

    def __init__(self):
        with open(os.getcwd() + "/config.yaml", "r") as f:
            self.config = yaml.safe_load(f)
        self.browser = browser

    def click_and_wait_for_element_state(self, target_locator, expected_element_locator, element_state: ElementState):
        self.browser.click(target_locator)
        self.browser.wait_for_elements_state(expected_element_locator, state=element_state)

