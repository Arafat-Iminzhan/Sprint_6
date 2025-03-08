from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage(BasePage):

    @allure.step('Клик на кнопку "Заказать" в шапке главной страницы')
    def click_header_order_btn(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(HomePageLocators.ORDER_BTN_HEADER))
        self.click_to_element(HomePageLocators.ORDER_BTN_HEADER)

    @allure.step('Клик на кнопку "Заказать" в середине главной страницы')
    def click_main_order_btn(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(HomePageLocators.ORDER_BTN_PAGE))
        self.click_to_element(HomePageLocators.ORDER_BTN_PAGE)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.NAME_FIELD))
        self.set_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.LAST_NAME_FIELD))
        self.set_text(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.ADDRESS_FIELD))
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбор станции метро')
    def set_metro(self, station_locator):
        """ Выбирает станцию метро """
        self.click_to_element(OrderPageLocators.METRO_FIELD)  # Открываем список

        if not isinstance(station_locator, tuple):
            raise ValueError(f"Неверный локатор для станции метро: {station_locator}")

        # Ожидаем появления станции в списке
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(station_locator)
        )

        self.click_to_element(station_locator)  # Выбираем станцию

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.PHONE_FIELD))
        self.set_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BTN))
        self.click_to_element(OrderPageLocators.NEXT_BTN)

    @allure.step('Выбор даты доставки')
    def set_date(self, date_locator):
        """ Открывает календарь, ожидает появления даты и выбирает её """
        self.click_to_element(OrderPageLocators.DATE_FIELD)  # Открываем календарь

        # Проверяем, что локатор передан правильно
        if not isinstance(date_locator, tuple):
            raise ValueError(f"Неверный локатор для даты: {date_locator}")

        try:
            # Ждём появления даты в DOM
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(date_locator)
            )

            # Прокручиваем страницу до даты
            self.scroll_to_element(date_locator)

            # Дожидаемся кликабельности
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(date_locator)
            )

            self.click_to_element(date_locator)  # Выбираем дату
            print(f"✅ Дата успешно выбрана: {date_locator}")
        except Exception as e:
            print(f"❌ Ошибка при выборе даты: {e}")
            raise Exception(f"Ошибка при выборе даты: {e}")  # Явно выбрасываем ошибку

    @allure.step('Выбор срока аренды')
    def set_term(self, term):
        self.click_to_element(OrderPageLocators.RENT_FIELD)  # Открываем выпадающий список
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(term))  # Ждём доступность срока
        self.click_to_element(term)  # Выбираем срок аренды

    @allure.step('Выбор цвета')
    def set_color(self, color):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(color))
        self.click_to_element(color)

    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.COMMENTS))
        self.set_text(OrderPageLocators.COMMENTS, comments)

    @allure.step('Появление модального окна "Заказ оформлен"')
    def check_success_order(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_WINDOW))
        return self.find_element(OrderPageLocators.ORDER_SUCCESS_WINDOW).text

    @allure.step('Проверка успешного создания заказа')
    def check_success_order(self):
        """ Проверяет, что появилось окно успешного оформления заказа """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_WINDOW)
        )
        success_message = self.find_element(OrderPageLocators.ORDER_SUCCESS_WINDOW).text
        return success_message.strip() if success_message else None

    @allure.step('Создание заказа')
    def create_order(self, name, last_name, address, station, phone, date, term, color, comments):
        """ Заполняет форму заказа и подтверждает его """
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station)
        self.set_phone(phone)
        self.click_next_btn()

        try:
            self.set_date(date)
        except Exception as e:
            print(f"❌ Критическая ошибка: дата не выбрана! {e}")
            return False  # Останавливаем тест

        self.set_term(term)
        self.set_color(color)
        self.set_comments(comments)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BTN)
        )
        self.click_to_element(OrderPageLocators.ORDER_BTN)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.YES_BTN)
        )
        self.click_to_element(OrderPageLocators.YES_BTN)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_WINDOW)
            )
            print("✅ Заказ успешно оформлен!")
        except TimeoutException:
            print("❌ Ошибка: модальное окно подтверждения не появилось!")
            raise Exception("Модальное окно подтверждения заказа не появилось!")
