from app.locators.realtime.panel_detail import PanelDetailLocatorRealtime
from app.pages.realtime.base import BasePage
from app.util.error import Error, PLATFORM
from selenium.common.exceptions import TimeoutException


class PageWallboardDetalhado(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_value_disponivel(self) -> int:
        try:
            return int(self.get_text(PanelDetailLocatorRealtime.operator_available))
        except TimeoutException:
            raise Error(PanelDetailLocatorRealtime.operator_available, 'TimeoutException', PLATFORM['realtime'], 'get_value_disponivel', 'PageWallboardDetalhado')
