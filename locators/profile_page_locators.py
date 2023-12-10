from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PROFILE_LINK = (By.XPATH, '//*[@href="/account/profile"]')

    ORDER_HISTORY_LINK = (By.XPATH, '//*[@href="/account/order-history"]')

    LOGOUT_BUTTON = (By.XPATH, '//*[contains(@class, "Account_button")]')

    ORDER_STATUS = (By.XPATH, '//p[text()="Выполнен"]')

    ORDER_NUMBER_IN_ORDER_HISTORY = (By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]')
