from selenium.webdriver.common.by import By


class HomePageLocators:
    COOKIES_BTN = By.ID, "rcc-confirm-button"
    QUESTION = By.XPATH, "//div[@id = 'accordion__heading-{}']"
    ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    LAST_QUESTION = By.XPATH, "(//div[contains(@id,'accordion__heading-')])[last()]"
    ORDER_BTN_HEADER = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    ORDER_BTN_PAGE = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    YANDEX_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
    SAMOKAT_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    ZEN_HOME_PAGE = 'https://dzen.ru/?yredirect=true'
