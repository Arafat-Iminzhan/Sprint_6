from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Возвращает URL текущей страницы")
    def get_current_page_url(self):
        """Возвращает текущий URL страницы"""
        return self.driver.current_url

    def open_url(self, url):
        """Открывает указанный URL"""
        self.driver.get(url)

    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url

    def wait_for_element_visible(self, locator, timeout=10):
        """Ожидает, пока элемент станет видимым"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=5):
        """Ожидает, пока элемент станет кликабельным"""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        """Находит элемент на странице и возвращает его"""
        return self.wait_for_element_visible(locator)

    def click_to_element(self, locator):
        """Кликает на элемент, предварительно ожидая его кликабельности"""
        element = self.wait_for_element_clickable(locator)
        element.click()

    def set_text(self, locator, text):
        """Ожидает и вводит текст в поле"""
        element = self.wait_for_element_clickable(locator)
        element.send_keys(text)

    def get_text(self, locator):
        """Ожидает и получает текст элемента"""
        return self.wait_for_element_visible(locator).text

    def scroll_to_element(self, locator):
        """Прокручивает страницу до нужного элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_navigating_url(self, url, timeout=10):
        """Ожидает, пока текущий URL изменится на указанный"""
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def get_cookies(self, locator):
        """Принимает cookies, если элемент присутствует"""
        self.wait_for_element_clickable(locator)
        self.click_to_element(locator)

    def tab_switch(self):
        """Переключается на вторую вкладку браузера"""
        self.driver.switch_to.window(self.driver.window_handles[1])
