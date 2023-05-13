from selenium.webdriver.common.keys import Keys
from app.locators.webphone.selected_client import SelectedClientLocatorWebphone
from app.pages.webphone.base import BasePage
from app.util.error import Error, PLATFORM
from selenium.common.exceptions import TimeoutException


class PageSelectClient(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def encontra_client(self, client_name):
        try:
            self.insert_text(SelectedClientLocatorWebphone.input_search_client, client_name, Keys.TAB)
        except TimeoutException:
            raise Error(SelectedClientLocatorWebphone.input_search_client, 'TimeoutException', PLATFORM['webphone'], 'encontra_client', 'PageSelecteClient')

    def click_client(self):
        try:
            self.click(SelectedClientLocatorWebphone.button_client)
        except TimeoutException:
            raise Error(SelectedClientLocatorWebphone.button_client, 'TimeoutException', PLATFORM['webphone'], 'click_client', 'PageSelecteClient')
