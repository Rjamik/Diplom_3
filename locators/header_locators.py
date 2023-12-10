from selenium.webdriver.common.by import By


class HeaderLocators:

    ACCOUNT_LINK = (By.XPATH, '//*[@href="/account"]')

    CONSTRUCTOR_LINK = (By.XPATH, '//p[text()="Конструктор"]/parent::a')

    ORDER_LIST_LINK = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')