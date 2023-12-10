import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data import Url
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if request.param == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get(Url.URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def make_order(driver):
    main_page = MainPage(driver)
    main_page.make_order()


@pytest.fixture(scope='function')
def login(driver, user_data):
    main_page = MainPage(driver)
    main_page.click_on_enter_account_button()
    login_page = LoginPage(driver)
    login_page.fill_email(user_data['email'])
    login_page.fill_password(user_data['password'])
    login_page.click_on_enter_button()