import allure
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestFeedPage:

    @allure.title('Проверка отображения созданного заказа в разделе "В работе"')
    def test_new_order_shown_in_work_list(self, driver, login):

        main_page = MainPage(driver)

        new_order = main_page.make_order()
        header_page = HeaderPage(driver)
        header_page.click_on_order_list()
        feed_page = FeedPage(driver)

        new_order_in_work = feed_page.get_order_number_in_work_list()
        assert new_order_in_work.lstrip('0') == new_order, \
            'После создания заказа его номер не появился в разделе "В работе"'

    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_get_order_details(self, driver):

        header_page = HeaderPage(driver)
        header_page.click_on_order_list()
        feed_page = FeedPage(driver)

        feed_page.click_on_order()

        assert feed_page.find_the_element(10, FeedPageLocators.BURGER_CONTENT_TITLE).is_displayed(), \
            'При клике на заказ не появилось всплывающее окно с деталями заказа'

    @allure.title('Проверка изменения счетчика "Выполнено за все время" после создания заказа')
    def test_change_total_orders_number(self, driver, login):

        main_page = MainPage(driver)

        header_page = HeaderPage(driver)
        header_page.click_on_order_list()
        feed_page = FeedPage(driver)

        total_number = feed_page.get_total_orders_number()
        header_page.click_on_constructor()

        main_page.make_order()
        header_page.click_on_order_list()

        new_total_number = feed_page.get_total_orders_number()

        assert int(new_total_number) == int(total_number) + 1, \
            'После создания заказа счетчик "Выполнено за все время" не увеличился'

    @allure.title('Проверка отображения заказа юзера в разделе "Лента заказов"')
    def test_find_order_in_order_list(self, driver, login, make_order):

        main_page = MainPage(driver)

        header_page = HeaderPage(driver)
        header_page.click_on_account()
        profile_page = ProfilePage(driver)

        profile_page.click_on_order_history_link()

        chosen_order = profile_page.get_order_number()
        header_page.click_on_order_list()
        feed_page = FeedPage(driver)

        wanted_order = feed_page.find_order_in_order_list(chosen_order)

        assert wanted_order.is_displayed(), \
            'Заказ юзера из раздела "История заказов" не отображается в разделе "Лента заказов"'

    @allure.title('Проверка изменения счетчика "Выполнено за сегодня" после создания заказа')
    def test_change_today_orders_number(self, driver, login):
        main_page = MainPage(driver)

        header_page = HeaderPage(driver)
        header_page.click_on_order_list()
        feed_page = FeedPage(driver)

        today_number = feed_page.get_today_orders_number()
        header_page.click_on_constructor()

        main_page.make_order()
        header_page.click_on_order_list()

        new_today_number = feed_page.get_today_orders_number()

        assert int(new_today_number) == int(today_number) + 1, \
            'После создания заказа счетчик "Выполнено за сегодня" не увеличился'
