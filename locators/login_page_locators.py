from selenium.webdriver.common.by import By


class LoginPageLocators:

    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    RESET_PASSWORD_LINK = (By.XPATH, '//*[@href="/forgot-password"]')

    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')