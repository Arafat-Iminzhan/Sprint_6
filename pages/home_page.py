from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure

from utils.urls import Urls


class HomePage(BasePage):

    @allure.step('Клик на вопрос')
    def click_question(self, number):
        method, locator = HomePageLocators.QUESTION
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.click_to_element((method, locator))

    @allure.step('Получение ответа')
    def get_answer(self, number):
        method, locator = HomePageLocators.ANSWER
        locator = locator.format(number)
        self.find_element((method, locator))
        return self.get_text((method, locator))

    @allure.step('Клик на Яндекс в шапке')
    def click_yandex_logo(self):
        self.click_to_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Клик на Самокат в шапке')
    def click_samokat_logo(self):
        self.click_to_element(HomePageLocators.SAMOKAT_LOGO)

    @allure.step("Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»")
    def open_home_page(self):
        self.open_url(Urls.HOME_PAGE)
        self.wait_element_visibility_of_element_located(HomePageLocators.COOKIES_BTN)

    @allure.step("Возвращает URL текущей страницы")
    def get_current_page_url(self):
        return self.driver.current_url
