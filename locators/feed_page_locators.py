from selenium.webdriver.common.by import By


class FeedPageLocators:

    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')

    ORDER_NUMBER_IN_WORK = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")

    COMPLETED_ORDERS_TOTAL = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')


    COMPLETED_ORDERS_TODAY = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')


    ORDER_LINK = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')

    BURGER_CONTENT_TITLE = (By.XPATH, '//p[text()="Cостав"]')

    NO_ORDERS_IN_WORK_TITLE = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')

    ORDER_NUMBER_IN_ORDER_LIST = (By.XPATH, '//p[text()="{}"]')