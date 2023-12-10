from selenium.webdriver.common.by import By


class MainPageLocators:

    ENTER_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')

    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    INGREDIENT_BUN = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')


    INGREDIENT_FILLING = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]')


    INGREDIENT_SAUCE = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]')


    INGREDIENT_COUNTER = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]')


    INGREDIENT_DETAILS_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')


    INGREDIENT_DETAILS_MODAL = (By.XPATH, '//*[contains(@class, "contentBox")]')


    ORDER_BASKET = (By.XPATH, '//ul[contains(@class,"basket")]')

    ORDER_NUMBER = (By.XPATH, '//*[contains(@class, "type_digits-large")]')


    DEFAULT_ORDER_NUMBER = (By.XPATH, '//h2[text()="9999"]')


    ORDER_STATUS_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')

    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
