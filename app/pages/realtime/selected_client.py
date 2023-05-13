from selenium.webdriver.common.keys import Keys
from app.locators.realtime.selected_client import SelectedClientLocatorRealtime
from app.pages.realtime.base import BasePage
from app.util.error import Error, PLATFORM
from selenium.common.exceptions import TimeoutException


class PageSelectedClient(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def insert_client(self):
        try:
            self.click(SelectedClientLocatorRealtime.select_list_client)
        except TimeoutException:
            raise Error(SelectedClientLocatorRealtime.select_list_client, 'TimeoutException', PLATFORM['realtime'], 'insert_client', 'PageSelectedClient')

    def insert_name_client(self, client_name):
        try:
            self.insert_text(SelectedClientLocatorRealtime.input_search_client, client_name, Keys.RETURN)
        except TimeoutException:
            raise Error(SelectedClientLocatorRealtime.input_search_client, 'TimeoutException', PLATFORM['realtime'], 'insert_name_client', 'PageSelectedClient')

    def click_button_entrar(self):
        try:
            self.click(SelectedClientLocatorRealtime.button_select_client)
        except TimeoutException:
            raise Error(SelectedClientLocatorRealtime.button_select_client, 'TimeoutException', PLATFORM['realtime'], 'click_button_entrar', 'PageSelectedClient')


