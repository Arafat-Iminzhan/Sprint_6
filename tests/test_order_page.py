from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from utils.test_data import YaScooterOrderMainBtn
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине главной страницы')
    def test_create_order_main_page_btn(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()

        # Принятие cookies (если нужно)
        home_page.wait_for_element_clickable(HomePageLocators.COOKIES_BTN)
        home_page.get_cookies(HomePageLocators.COOKIES_BTN)

        order_page = OrderPage(driver)

        # Ожидание и клик по кнопке "Заказать" в середине страницы
        order_page.wait_for_element_clickable(HomePageLocators.ORDER_BTN_PAGE)
        order_page.click_main_order_btn()

        # Заполнение формы заказа
        order_page.create_order(YaScooterOrderMainBtn.first_name,
                                YaScooterOrderMainBtn.last_name,
                                YaScooterOrderMainBtn.address,
                                OrderPageLocators.STATION_2,
                                YaScooterOrderMainBtn.phone,
                                OrderPageLocators.DATE_2,
                                OrderPageLocators.TERM_2,
                                OrderPageLocators.GREY_COLOR,
                                YaScooterOrderMainBtn.comment)

        # Ожидание появления модального окна "Заказ оформлен"
        order_page.wait_for_element_visible(OrderPageLocators.ORDER_SUCCESS_WINDOW, timeout=15)

        # Проверка текста в окне подтверждения
        text = order_page.get_text(OrderPageLocators.ORDER_SUCCESS_WINDOW)
        assert 'Заказ оформлен' in text, "Ошибка: модальное окно 'Заказ оформлен' не появилось"
