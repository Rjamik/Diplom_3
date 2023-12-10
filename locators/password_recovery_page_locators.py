from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    RESET_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')

    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')

    SHOW_PASSWORD_ICON = (By.XPATH, '//div[contains(@class,"icon-action")]')

    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')

    INPUT_PASSWORD_ACTIVE = (By.CSS_SELECTOR, '.input.input_status_active')