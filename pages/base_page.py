from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))


    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    def wait_element_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))


    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text


    def set_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)


    def scroll(self, locator):
        element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def get_cookies(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).click()


    def wait_navigating_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))


    def tab_switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def scroll_to_element(self, locator):
        """Прокручивает страницу до нужного элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
