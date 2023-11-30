from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'

    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'

    SHOW_PASSWORD_ICON = By.XPATH, '//div[contains(@class,"icon-action")]'
