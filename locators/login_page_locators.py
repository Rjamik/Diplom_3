from selenium.webdriver.common.by import By


class LoginPageLocators:

    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'

    RESET_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'