from selenium.webdriver.common.by import By


class LoginLocatorWebphone:
    input_email = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/input[1]')
    input_password = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/input[2]')
    button = (By.XPATH, '//*[@id="root"]/div/div/div[1]/form/button')
