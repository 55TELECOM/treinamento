import os
from app.tests.realtime.webdriver import WebdriverSetup
from ddt import data, ddt, unpack, file_data
from app.pages.realtime.panel_detail import PageWallboardDetalhado
from app.util.error import Error
from time import sleep

@ddt
class PanelDetailTestRealtime(WebdriverSetup):

    @file_data(os.path.join(os.path.dirname(__file__), '../../mock/branch/user.json'))
    def test_get_operator_available(self, branchs):
        try:
            branch_number = branchs[0]
            self.logger.info(f'Iniciando o teste: test_get_operator_available com o valores: {branch_number["email"]}, {branch_number["password"]}, {branch_number["client_name"]}')
            self.login_realtime(branch_number['email'], branch_number['password'], branch_number['client_name'])

            page_wallboard_detail = PageWallboardDetalhado(self.driver)
            count_operator_available = page_wallboard_detail.get_value_disponivel()

            self.assertEqual(count_operator_available, 0)
        except Error as value:
            self.logger.error(value.message())
            self.fail(value.message())
        except Exception as value:
            self.logger.error(f'Error {value}')
            self.fail(value)

    @file_data(os.path.join(os.path.dirname(__file__), '../../mock/branch/user.json'))
    def test_get_operator_available_different_zero(self, branchs):
        try:
            branch_number_realime = branchs[0]
            branch_number_webphone = branchs[1]

            self.logger.info(
                f'Iniciando o teste: test_get_operator_available com o valores: {branch_number_realime["email"]} {branch_number_realime["password"]} {branch_number_realime["client_name"]}'
            )

            self.login_realtime(branch_number_realime['email'], branch_number_realime['password'], branch_number_realime['client_name'])
            self.login_webphone(branch_number_webphone['email'], branch_number_webphone['password'], branch_number_webphone['client_name'])
            sleep(5)

            page_wallboard_detail = PageWallboardDetalhado(self.driver)

            count_operator_available = page_wallboard_detail.get_value_disponivel()
            self.assertNotEqual(count_operator_available, 0)
        except Error as value:
            self.logger.error(value.message())
            self.fail(value.message())
        except Exception as value:
            self.logger.error(f'Error {value}')
            self.fail(value)

