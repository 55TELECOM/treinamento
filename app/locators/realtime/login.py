from selenium.webdriver.common.by import By


class LoginLocatorRealtime:
    input_email = (By.XPATH, '//*[@id="form_email"]')
    input_password = (By.XPATH, '//*[@id="form_password"]')
    button = (By.XPATH, '//*[@id="color_trans_button"]')
