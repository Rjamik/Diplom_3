from selenium.webdriver.common.by import By


class BasePageLocators:

    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'


    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'


    INPUT_PASSWORD_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'

    CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
