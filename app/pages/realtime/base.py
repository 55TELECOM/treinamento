from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    def insert_text(self, locator, text, key=None, time=10):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        element.send_keys(text)

        if key:
            element.send_keys(key)

    def get_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).text