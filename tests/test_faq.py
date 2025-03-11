from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
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


        # Прокрутка до последнего вопроса (чтобы избежать проблем с видимостью)
        home_page.scroll_to_element(HomePageLocators.LAST_QUESTION)

        # Формируем правильный локатор вопроса
        question_locator = (HomePageLocators.QUESTION[0], HomePageLocators.QUESTION[1].format(number))

        # Ожидание кликабельности и клик по вопросу
        home_page.wait_for_element_clickable(question_locator)
        home_page.click_question(number)

        # Формируем правильный локатор ответа
        answer_locator = (HomePageLocators.ANSWER[0], HomePageLocators.ANSWER[1].format(number))

        # Ожидание появления ответа
        home_page.wait_for_element_visible(answer_locator)
        answer = home_page.get_text(answer_locator)

        assert answer == expected_answer, f"Ожидали: '{expected_answer}', получили: '{answer}'"
