from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure
from utils.urls import Urls

class HomePage(BasePage):

    @allure.step('Клик на вопрос')
    def click_question(self, number):
        """Кликает на нужный вопрос из списка FAQ"""
        method, locator = HomePageLocators.QUESTION
        formatted_locator = (method, locator.format(number))
        self.click_to_element(formatted_locator)  # Уже включает ожидание кликабельности

    @allure.step('Получение ответа')
    def get_answer(self, number):
        """Возвращает текст ответа на вопрос FAQ"""
        method, locator = HomePageLocators.ANSWER
        formatted_locator = (method, locator.format(number))
        return self.get_text(formatted_locator)  # Уже включает ожидание видимости

    @allure.step('Клик на Яндекс в шапке')
    def click_yandex_logo(self):
        """Кликает по логотипу Яндекс в шапке сайта"""
        self.click_to_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Клик на Самокат в шапке')
    def click_samokat_logo(self):
        """Кликает по логотипу Самокат в шапке сайта"""
        self.click_to_element(HomePageLocators.SAMOKAT_LOGO)

    @allure.step("Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»")
    def open_home_page(self):
        """Открывает главную страницу и ожидает появления кнопки cookies"""
        self.open_url(Urls.HOME_PAGE)
        self.wait_for_element_visible(HomePageLocators.COOKIES_BTN)
