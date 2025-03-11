from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
import allure
import logging

# Настраиваем логгер
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class OrderPage(BasePage):

    @allure.step('Клик на кнопку "Заказать" в шапке главной страницы')
    def click_header_order_btn(self):
        self.click_to_element(HomePageLocators.ORDER_BTN_HEADER)

    @allure.step('Клик на кнопку "Заказать" в середине главной страницы')
    def click_main_order_btn(self):
        self.click_to_element(HomePageLocators.ORDER_BTN_PAGE)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбор станции метро')
    def set_metro(self, station_locator):
        """Выбирает станцию метро"""
        self.click_to_element(OrderPageLocators.METRO_FIELD)  # Открываем список
        if not isinstance(station_locator, tuple):
            raise ValueError(f"Неверный локатор для станции метро: {station_locator}")
        self.click_to_element(station_locator)  # Выбираем станцию

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        self.click_to_element(OrderPageLocators.NEXT_BTN)

    @allure.step('Выбор даты доставки')
    def set_date(self, date_locator):
        """Открывает календарь, ожидает появления даты и выбирает её"""
        try:
            self.click_to_element(OrderPageLocators.DATE_FIELD)  # Открываем календарь
            self.click_to_element(date_locator)  # Выбираем дату
            logger.info(f"✅ Дата успешно выбрана: {date_locator}")
        except Exception as e:
            logger.error(f"❌ Ошибка при выборе даты: {e}", exc_info=True)
            raise

    @allure.step('Выбор срока аренды')
    def set_term(self, term):
        self.click_to_element(OrderPageLocators.RENT_FIELD)
        self.click_to_element(term)

    @allure.step('Выбор цвета')
    def set_color(self, color):
        self.click_to_element(color)

    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        self.set_text(OrderPageLocators.COMMENTS, comments)

    @allure.step('Появление модального окна "Заказ оформлен"')
    def check_success_order(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_WINDOW)

    @allure.step('Создание заказа')
    def create_order(self, name, last_name, address, station, phone, date, term, color, comments):
        """Заполняет форму заказа и подтверждает его"""
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station)
        self.set_phone(phone)
        self.click_next_btn()

        try:
            self.set_date(date)
        except Exception as e:
            logger.critical(f"❌ Критическая ошибка: дата не выбрана! {e}")
            return False

        self.set_term(term)
        self.set_color(color)
        self.set_comments(comments)

        self.click_to_element(OrderPageLocators.ORDER_BTN)
        self.click_to_element(OrderPageLocators.YES_BTN)

        try:
            success_message = self.check_success_order()
            logger.info("✅ Заказ успешно оформлен!")
            return success_message
        except Exception as e:
            logger.error("❌ Ошибка: модальное окно подтверждения не появилось!", exc_info=True)
            raise Exception("Модальное окно подтверждения заказа не появилось!")
