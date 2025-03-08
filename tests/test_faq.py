from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from conftest import driver
from utils.test_data import YaScooterHomePageFAQ
import pytest
import allure


class TestQuestionsHomePage:
    @allure.title('Проверка ответов на вопросы из выпадающего списка «Вопросы о важном»')
    @pytest.mark.parametrize('number, expected_answer', YaScooterHomePageFAQ.answers)
    def test_question(self, driver, number, expected_answer):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.get_cookies(HomePageLocators.COOKIES_BTN)
        home_page.scroll(HomePageLocators.LAST_QUESTION)
        home_page.click_question(number)
        answer = home_page.get_answer(number)
        assert answer == expected_answer
