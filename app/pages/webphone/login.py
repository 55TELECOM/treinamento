from app.locators.webphone.login import LoginLocatorWebphone
from app.pages.webphone.base import BasePage
from app.util.error import Error, PLATFORM
from selenium.common.exceptions import TimeoutException


class WebphonePageLogin(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def insert_email(self, email):
        try:
            self.insert_text(LoginLocatorWebphone.input_email, email)
        except TimeoutException:
            raise Error(LoginLocatorWebphone.input_email, 'TimeoutException', PLATFORM['webphone'], 'insert_email', 'WebphoneṔageLogin')

    def insert_password(self, password):
        try:
            self.insert_text(LoginLocatorWebphone.input_password, password)
        except TimeoutException:
            raise Error(LoginLocatorWebphone.input_password, 'TimeoutException', PLATFORM['webphone'], 'insert_password', 'WebphoneṔageLogin')

    def click_entar(self):
        try:
            self.click(LoginLocatorWebphone.button)
        except TimeoutException:
            raise Error(LoginLocatorWebphone.button, 'TimeoutException', PLATFORM['webphone'], 'click_entar', 'WebphoneṔageLogin')
