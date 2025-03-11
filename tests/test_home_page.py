from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from utils.urls import Urls
import allure


class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке возвращает на главную страницу')
    def test_redirect_samokat_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()

        # Ожидание кликабельности и клик по кнопке "Заказать" в шапке
        home_page.wait_for_element_clickable(HomePageLocators.ORDER_BTN_HEADER)
        home_page.click_to_element(HomePageLocators.ORDER_BTN_HEADER)

        # Клик по логотипу "Самокат" для возврата на главную страницу
        home_page.click_samokat_logo()

        # Ожидание загрузки главной страницы
        home_page.wait_navigating_url(Urls.HOME_PAGE)

        # Проверка URL
        assert home_page.get_current_url() == Urls.HOME_PAGE, "Ошибка: не произошло редиректа на главную страницу"

    @allure.title('Проверка редиректа на Dzen.ru при клике на Яндекс в лого шапки')
    def test_redirect_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()

        # Клик по логотипу "Яндекс"
        home_page.click_yandex_logo()

        # Переключение на новую вкладку
        home_page.tab_switch()

        # Ожидание загрузки страницы Dzen.ru
        home_page.wait_navigating_url(Urls.ZEN_HOME_PAGE)

        # Проверка URL
        assert home_page.get_current_url() == Urls.ZEN_HOME_PAGE, "Ошибка: не произошло редиректа на Dzen.ru"
