from selenium.webdriver.common.by import By


class FeedPageLocators:

    ORDERS_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'

    ORDER_NUMBER_IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'

    COMPLETED_ORDERS_TOTAL = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'


    COMPLETED_ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'


    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    BURGER_CONTENT_TITLE = By.XPATH, '//p[text()="Cостав"]'

    NO_ORDERS_IN_WORK_TITLE = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'


    ORDER_NUMBER_IN_ORDER_LIST = By.XPATH, '//p[text()="{}"]'