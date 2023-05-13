import unittest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.pages.realtime.login import PageLoginRealtime
from app.pages.realtime.selected_client import PageSelectedClient
from app.pages.webphone.login import WebphonePageLogin
from app.pages.webphone.selected_client import PageSelectClient


class WebdriverSetup(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        self.driver = webdriver.Chrome()
        self.driver.get('https://realtimebeta.55pbx.com:8600')

        if self._testMethodName.startswith('test_get_operator_available_different_zero'):
            options = Options()
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("prefs", {
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.geolocation": 1,
                "profile.default_content_setting_values.notifications": 1
            })

            self.driver_webphone = webdriver.Chrome(options=options)
            self.driver_webphone.get('https://fonebeta.55pbx.com')

    def login_realtime(self, email, password, client_name):
        page_login_realtime = PageLoginRealtime(self.driver)
        page_login_realtime.insert_input_email(email)
        page_login_realtime.insert_input_password(password)
        page_login_realtime.click_button_entrar()

        page_selected_client = PageSelectedClient(self.driver)
        page_selected_client.insert_client()
        page_selected_client.insert_name_client(client_name)
        page_selected_client.click_button_entrar()

    def login_webphone(self, email, password, client_name):
        page_login_webphone = WebphonePageLogin(self.driver_webphone)
        page_login_webphone.insert_email(email)
        page_login_webphone.insert_password(password)
        page_login_webphone.click_entar()

        page_selected_client_webphone = PageSelectClient(self.driver_webphone)
        page_selected_client_webphone.encontra_client(client_name)
        page_selected_client_webphone.click_client()

    def tearDown(self) -> None:
        # ele é executado a cada final de um teste
        if self.driver is not None:
            self.driver.close()

        if self._testMethodName.startswith('test_get_operator_available_different_zero'):
            if self.driver_webphone is not None:
                self.driver_webphone.close()

