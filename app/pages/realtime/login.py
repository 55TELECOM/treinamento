from app.locators.realtime.login import LoginLocatorRealtime
from app.pages.realtime.base import BasePage
from selenium.common.exceptions import TimeoutException
from app.util.error import Error, PLATFORM


class PageLoginRealtime(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def insert_input_email(self, email):
        try:
            self.insert_text(LoginLocatorRealtime.input_email, email)
        except TimeoutException:
            raise Error(LoginLocatorRealtime.input_email, 'TimeoutException', PLATFORM['realtime'], 'insert_input_email', 'PageLoginRealtime')

    def insert_input_password(self, password):
        try:
            self.insert_text(LoginLocatorRealtime.input_password, password)
        except TimeoutException:
            raise Error(LoginLocatorRealtime.input_password, 'TimeoutException', PLATFORM['realtime'], 'insert_input_password', 'PageLoginRealtime')

    def click_button_entrar(self):
        try:
            self.click(LoginLocatorRealtime.button)
        except TimeoutException:
            raise Error(LoginLocatorRealtime.button, 'TimeoutException', PLATFORM['realtime'], 'click_button_entrar', 'PageLoginRealtime')
